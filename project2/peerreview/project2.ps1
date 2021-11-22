while($true) {
    $Memory = Get-ComputerInfo  -Property "OsFreeVirtualMemory"
    Get-Date
    $variable.property
    $Memory = $Memory.OsFreeVirtualMemory
    write-host "Your System has $Memory bytes of memory left."
    
    
    out-file C:\Memory\Memoryleft.txt 
    
    Start-Sleep -s 86400
    }
