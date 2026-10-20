"""Validate published catalog consistency and offline planning, not omitted sources."""
import json
import subprocess
import sys
from pathlib import Path
from plan import plan
ROOT = Path(__file__).resolve().parent

def main():
    m = json.loads((ROOT / "manifest.json").read_text())
    assert m["live_tested"] is False
    assert m["route_declaration_count"] == len(m["routes"])
    assert m["unique_route_literal_count"] == len({r["path_literal"] for r in m["routes"]})
    assert m["model_count"] == len(m["models"])
    assert all(r["http_method"] == "GET" for r in m["routes"])
    actual = list(plan(m))
    assert len(actual) == len(set(actual))
    assert all(x.startswith("GET <VERIFIED_NATIVE_BASE_HOST>/") for x in actual)
    assert all("\\u200b" not in x and "\u200b" not in x for x in actual)
    synthetic = {"routes": [
        {"http_method": "POST", "path_literal": "synthetic-write", "unsafe_literal": False, "parameters": []},
        {"http_method": "GET", "path_literal": "synthetic-bad\\u200b", "unsafe_literal": True, "parameters": []}]}
    assert list(plan(synthetic)) == []
    output = subprocess.check_output([sys.executable, str(ROOT / "plan.py"), "--plan"], text=True)
    assert output.count("\nGET ") == len(actual)
    print(json.dumps({"result": "PASS", "scope": "published catalog and planner only; APK/source/REA evidence NOT checked",
                      "get_declarations": len(m["routes"]), "distinct_get_literals": m["unique_route_literal_count"],
                      "model_entries": len(m["models"]), "planned_templates": len(actual), "live_requests": 0}, indent=2))

if __name__ == "__main__":
    main()
