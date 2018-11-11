$boots = Get-EventLog -Log System -Source Microsoft-Windows-Kernel-Boot -InstanceID 25 -Newest 10
$boots | Select -Property TimeGenerated
