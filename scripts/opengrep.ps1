<#
.SYNOPSIS
  Run Opengrep on src/ and tests/ with the local rules. Run it before every push.
#>
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$og = Join-Path $HOME '.opengrep\cli\latest\opengrep.exe'
Set-Location $root
& $og scan --config opengrep-rules.yml --error src tests
exit $LASTEXITCODE
