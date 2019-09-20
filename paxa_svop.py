class opensavefl:

    def __init__(self,old):
        ""
        self.old                    =   old

    def op_disp(self):
        ""

        name        =   self.old.gril_open['OPEN']["var"]['p']
        ra_op       =   self.old.gril_open['OPEN']  #<--- raco
        ra          =   self.old.pad[name]          #<--- raco
        
        ra_op['var']["home"].append("open")
        ra_op["m_pos"]                      =   {}
        ra_op['var']['fl']                  =   "paxa_save/paxa_sv.txt"
        ra_op['var'][name]['disp']          =   {'row':8,'size':50,
                                                    'ajt':[0,0],"px_c":[0,0]}
        
        ra['ajt']                           =   [0,0]
        ra['taile']                         =   100
        ra["pos"][(0,0)]["size"]            =   [0,0]
        ra["pos"][(0,0)]["szc"]             =   [-0,-0]

        self.old.svme.open_on(ra_op['var']['fl'],name)
        self.old.gril_d["d"]["g"]          =   self.old.gril_open
        #self.old.gril_d['n']['v']           =   2

    def op_save(self,fl):
        ""
        name        =   self.old.gril_open['OPEN']["var"]['p']
        ra_op       =   self.old.gril_open['OPEN']  #<--- raco
        ra          =   self.old.pad[name]          #<--- raco
        ra_op['var']["home"].append("save")
        ra_op['var']['fl']                  =   fl
        self.old.svme.save_gril(self.old.gril_game,ra_op["var"]["fl"])
        self.old.svme.open_off()
        ra_op['var'][name]['but_app']       =   {}

    def op_dire(self):
        ""
        name        =   self.old.gril_open['OPEN']["var"]['p']
        ra_op       =   self.old.gril_open['OPEN']  #<--- raco
        ra          =   self.old.pad[name]          #<--- raco
        ax,ay                               =   ra["ajt"]
        self.old.gril_game                  =   ra_op['fl'][(ax,ay)]["nana"]
        self.old.svme.open_off()
        #self.old.gril_game           =   ra_op['fl'][(ax,ay)]["nana"]
        #self.old.gril_d["n"]["g"] = self.old.gril_game 
        

    def op_d(self):
        ""
        name        =   self.old.gril_open['OPEN']["var"]['p']
        ra_op       =   self.old.gril_open['OPEN']  #<--- raco
        ra          =   self.old.pad[name]          #<--- raco
        ax,ay                               =   ra["ajt"]
        if ra_op["fl"].keys().count((ax,ay)) ==0:ra["ajt"] =[0,0]
        ax,ay                               =   ra["ajt"]
        self.old.gril_d["d"]["g"]           =   ra_op['fl'][(ax,ay)]["nana"]
        #print ra_op['fl'][(ax,ay)]['nfl']
        
        
        
