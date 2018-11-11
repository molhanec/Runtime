$shutdows = Get-EventLog -Log System -Source Microsoft-Windows-Kernel-Power -InstanceID 42 -Newest 9
$shutdows | Select -Property TimeGenerated
