Configuration Computer_RenameComputer_Config
{
    Import-DscResource -Module ComputerManagementDsc

    Node localhost
    {
        Computer NewName
        {
            Name = 'englejc-winn'
        }
    }
}