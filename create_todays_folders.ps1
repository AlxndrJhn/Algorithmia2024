# if the first argument is a number, use that as the day number, with leading 0
# otherwise, use today's date
if ($args[0] -match "^\d+$") {
    $todayAsNumNoLeadingZero = $args[0].ToString()
}
else {
    $todayAsNumNoLeadingZero = (Get-Date).ToString("dd").Trim('0')
}
$todayAsPaddedNum = $todayAsNumNoLeadingZero.PadLeft(2, '0')

# copy template to new folder
Copy-Item -r template "$todayAsPaddedNum"

code "$todayAsPaddedNum/input.txt"
code "$todayAsPaddedNum/day.py"
code "$todayAsPaddedNum/input_example.txt"

# open chrome browser
Start-Process chrome "https://everybody.codes/event/2024/quests/$todayAsNumNoLeadingZero"
