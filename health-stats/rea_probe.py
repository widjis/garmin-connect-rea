"""Local REA metadata probe. Requires caller-provided engine/JDK/JAR paths."""
import asyncio
import json
import os
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
ROOT = Path(__file__).resolve().parent

async def main():
    env = dict(os.environ)
    for name in ("JAVA_HOME", "REA_JADX_MCP_JAR", "REA_ENTRYPOINT"):
        if not env.get(name):
            raise SystemExit("Set " + name + " to a separately installed local dependency")
    env["REA_JADX_HEAP_MIB"] = "6144"
    env["REA_JADX_ACTIVE_PROCESSOR_COUNT"] = "2"
    params = StdioServerParameters(command=env.get("REA_NODE", "node"),
                                   args=[env["REA_ENTRYPOINT"], "--mcp"], env=env)
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write, read_timeout_seconds=300) as session:
            await session.initialize()
            result = await session.call_tool("inspect_android_package", {"path": str(ROOT.parent / "apk/base.apk")})
            out = ROOT / "evidence"
            out.mkdir(parents=True, exist_ok=True)
            (out / "rea-package.json").write_text(json.dumps(result.model_dump(mode="json", by_alias=True), indent=2))
            print("REA package inspection completed; inspect ignored local evidence for tool errors.")

if __name__ == "__main__":
    asyncio.run(main())
