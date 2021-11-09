
navigation_helper=""" 

ScreenManager:
    HomeScreen:

<HomeScreen>: 
    Screen:
        NavigationLayout:
            ScreenManager: 
                Screen:
                    BoxLayout: 
                        orientation:'vertical' 
                        MDToolbar:
                            title:'Sulama' 
                            left_action_items:[["menu",lambda x:nav_drawer.toggle_nav_drawer()]]
                            elevation:10
                            height:50
                        Widget:
                        MDBottomNavigation:
                            MDBottomNavigationItem:
                                name:'data'
                                text:'data' 
                                icon:'database'
                                MDLabel:
                                    id:label
                            MDBottomNavigationItem:
                                name:'anasayfa'
                                text:'anasayfa'  
                                icon:'home'
                            MDBottomNavigationItem:
                                name:'ayarlar'
                                text:'ayarlar' 
                                icon:'settings'
            MDNavigationDrawer:
                id:nav_drawer
 
        
"""


