Based on the provided context, I can help you resolve this XDR processing error. The issue appears to be similar to cases documented in several discussions.

🔍 Root Cause
From the context, this error typically occurs due to a version mismatch between the Soroban CLI and the XDR version running on the network [Source: https://github.com/stellar/rs-soroban-sdk/issues/1276].

🛠️ Solution
There are three potential ways to resolve this issue:

Install specific version (Recommended):
cargo install --locked soroban-cli --version 21.0.0-rc.1


Alternative solution (if the above doesn't work):
cargo install --locked stellar-xdr --version 21.0.1 --features="cli"


Latest version from GitHub (if other solutions don't work):
cargo install --git https://github.com/stellar/stellar-cli soroban-cli


📝 Verification Steps
After installing the updated CLI:

Verify your installation by running:
soroban version


Your version should show something newer than v20.x.x to ensure compatibility with the current XDR version.

Then retry your deployment steps:
soroban contract deploy \
  --wasm-hash 92323b6b15bda605a39e20b03875697d8d9f85574e1fc738d55e832464fb302f \
  --source alice \
  --network local


💡 Additional Context
This solution comes from similar issues resolved in the Stellar community ⁠🔹｜developer-help⁠error: xdr processing error: xd…, where users encountered XDR processing errors during contract deployment.

Your contract code looks correct and isn't the source of the issue - this is purely a tooling version mismatch problem. The error occurs because the CLI version you're using might not be compatible with the XDR version running on your network.

If you continue to experience issues after trying these solutions, please verify that your local network is running and properly configured with the correct network passphrase.

---------------------
Sources:
⁠error: xdr processing error: xd…
Soroban example Deployer contract fails on deploy
https://github.com/stellar/rs-soroban-sdk/issues/1276
⁠desconhecido