'''
You are participating in an online chess tournament. There is a chess round that starts every 15 minutes. The first round of the day starts at 00:00, and after every 15 minutes, a new round starts.

For example, the second round starts at 00:15, the fourth round starts at 00:45, and the seventh round starts at 01:30.
You are given two strings loginTime and logoutTime where:

loginTime is the time you will login to the game, and
logoutTime is the time you will logout from the game.
If logoutTime is earlier than loginTime, this means you have played from loginTime to midnight and from midnight to logoutTime.

Return the number of full chess rounds you have played in the tournament.

Note: All the given times follow the 24-hour clock. That means the first round of the day starts at 00:00 and the last round of the day starts at 23:45.

 
 '''
class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        login = self.to_min(loginTime)
        logout = self.to_min(logoutTime)
        
        if logout < login:  # new day after midnight
            logout = logout + 24 * 60
            
        if logout - login < 15:
            return 0
        
        login = self.round_login(login)
        logout = self.round_logout(logout)
        
        return (logout - login) // 15
    
    
    def to_min(self, current_time: str) -> int:
        h, m = map(int, current_time.split(":"))
        return h * 60 + m
    
    def round_login(self, m: int):
        return m if m % 15 == 0 else m + (15 - m % 15)
    
    def round_logout(self, m: int):
        return m if m % 15 == 0 else m - (m % 15)
