class Arsenal:
    def gunners(self):
        print("- No.1 in the EPL right now")

class ManCity:
    def cityzens(self):
        print("- Reigning champions in the EPL but no.2 in the league right now")
     
class ManUtd:
    def reddevils(self):
        print("- No.3 in the EPL and recently became carabao cup winners")

class Liverpool:
    def ynwa(self):
        print("- No.5 in the EPL but won 7-0 against Man Utd  at anfield against Liverpool")

class News(Arsenal, ManCity, ManUtd, Liverpool):
    def league(self):
        print("- Man Utd lost 7-0 at Anfield 5th March 2023")

n = News()
n.league()
n.gunners()
n.cityzens()
n.reddevils()
n.ynwa()