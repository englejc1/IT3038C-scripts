function getIP{
    (Get-NetIPAddress).ipv4address | Select-String "192*"
}

Write-Host(getIP)
$IP = getIP
$Date = ""
$Body = "This machine's IP is $IP. User is $env:username. Hostname is $. PowerShell Version . Today's date is $Date"

write-host($Body)