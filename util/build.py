# Copyright (c) 2021 Valerio Colella
# SPDX-License-Identifier: MIT

import requests, json

SPDX_LICENSES_URL = "https://spdx.org/licenses/licenses.json"

def main():

    finallicenses = {}
    licensedata: list[dict] = requests.get(SPDX_LICENSES_URL).json()["licenses"]

    for license in licensedata:

        if not license["isDeprecatedLicenseId"]:
            name = license["name"]
            ref = license["reference"]
            license_id = license["licenseId"]

            finallicenses[name] = {
                "prefix": f"SPDX-{license_id}",
                "body": f"$LINE_COMMENT SPDX-License-Identifier: {license_id}",
                "description": f"{name}\n{ref}"
            }
    
    with open("../snippets/snippets.code-snippets", "w") as f:
        f.write(json.dumps(finallicenses, indent=4, sort_keys=True))
            

if __name__ == "__main__":
    main()