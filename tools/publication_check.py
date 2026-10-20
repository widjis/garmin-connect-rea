"""Check the reviewed publication allowlist, hashes and common secret patterns.
This is a publication guard, not proof that arbitrary text contains no sensitive data.
"""
import hashlib
import json
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
INDEX = "publication-manifest.json"
PATTERNS = {
    "JWT": re.compile(r"eyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}"),
    "provider token": re.compile(r"(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[A-Z0-9]{16})"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "literal credential": re.compile(r"(?i)(?:access_token|refresh_token|password|passwd|client_secret|api_key)\s*[=:]\s*[\"'][A-Za-z0-9_./+=-]{8,}[\"']"),
    "literal bearer": re.compile(r"(?i)Bearer\s+[A-Za-z0-9_.=-]{20,}"),
    "email": re.compile(r"[A-Za-z0-9_.+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "machine home path": re.compile(r"/(?:Users|home)/[A-Za-z0-9_.-]+/"),
}
FORBIDDEN_PARTS = {".private", ".venv", "apk", "dex", "sources", "auth-sources", "evidence"}
FORBIDDEN_SUFFIXES = {".apk", ".dex", ".jar", ".class", ".log"}

def main():
    index = json.loads((ROOT / INDEX).read_text())
    expected = index["files"]
    actual = {str(p.relative_to(ROOT)): p for p in ROOT.rglob("*")
              if p.is_file() and not any(x in p.relative_to(ROOT).parts for x in (".git", "__pycache__"))}
    issues = []
    if set(actual) != set(expected) | {INDEX}:
        issues.append("Publication file set differs from reviewed allowlist")
    for rel, info in expected.items():
        p = actual.get(rel)
        if p is None:
            continue
        if p.is_symlink() or FORBIDDEN_PARTS.intersection(p.relative_to(ROOT).parts) or p.suffix in FORBIDDEN_SUFFIXES or p.name.startswith(".env"):
            issues.append(rel + ": forbidden publication input")
        data = p.read_bytes()
        if hashlib.sha256(data).hexdigest() != info["sha256"] or len(data) != info["bytes"]:
            issues.append(rel + ": content differs from reviewed hash")
        text = data.decode("utf-8")
        for label, pattern in PATTERNS.items():
            if pattern.search(text):
                issues.append(rel + ": " + label)
    if issues:
        print(json.dumps({"result": "FAIL", "issues": issues}, indent=2))
        raise SystemExit(1)
    print(json.dumps({"result": "PASS", "reviewed_files": len(expected), "total_files": len(actual),
                      "reviewed_bytes": sum(x["bytes"] for x in expected.values()),
                      "checks": ["explicit file allowlist", "SHA-256 and byte counts", "excluded inputs", "common secret patterns"],
                      "limitation": "Pattern scans supplement manual privacy review; not an exhaustive secret detector"}, indent=2))

if __name__ == "__main__":
    main()
