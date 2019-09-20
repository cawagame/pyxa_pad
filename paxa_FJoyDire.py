class funct:
    "fonction joy"

    def __init__(self,old):
        ""
        self.old                                    =   old

    def dire(self,i,pax):
        ""
        rac                                         =   self.old.pad[i]['joy']
        ra                                          =   self.old.pad[i]
        if pax[0]                   !="a":
            if 1<= pax[1] <=4:
                v_exe       = "self.old."+ra['pad_pos'][pax[1]]
                exec(v_exe)
                return 1
      
                if ra['module']['n_color']['on']   ==1:
                    a,b             =   m_palcl.curseur['ajt']
                    c,d             =   m_palcl.pal_cl['ajt']
                    e               =   (a+c,b+d)
                    f               =   m_palcl.pal_cl['m_pos'].keys().count(e)
                    m_palcl.curseur['var']              =   None
                    if f==1:m_palcl.curseur['var']      =   m_palcl.pal_cl['m_pos'][e]
                    self.old.but_app['app_cl']['on']    =   1
                    self.old.but_app['app_cl']['play']  =   i
                    self.old.but_app['app_cl']['n_butt']=   m_palcl.curseur['var']['cl'] 
