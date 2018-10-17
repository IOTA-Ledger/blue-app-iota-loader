import os

python_venv = "python"
target_id   = 0x31100003
script_cmd  = "-m ledgerblue.deleteApp --targetId 0x%08X --appName \"IOTA\"" % (target_id)

os.system("%s %s" % (python_venv, script_cmd))
