# take the wiki data and translate it to json format

# turn the data into a nice readable format (json standard)
def parse_aram(aram_data):
    aram_data = aram_data.replace('=', '', 1)
    aram_data = aram_data.replace('[', '')
    aram_data = aram_data.replace(']', '')
    aram_data = aram_data.replace('=', ':')
    aram_data = aram_data.rsplit(',', 1)[0]
    str(aram_data).rsplit()
    return aram_data
class Champion:

    def __init__(self, champ_id, name, title, aram_data):
        self.champ_id = champ_id
        self.name = name
        self.title = title
        self.aram_data = parse_aram(aram_data)+"\n"
        # print(aram_data)

    # to string
    def str(self):
        return "Champion ID: {}\nName: {}\nAram stats: {}".format(self.champ_id, self.name+", "+self.title, self.aram_data)
