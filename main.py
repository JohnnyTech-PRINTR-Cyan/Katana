from flaskwebgui import FlaskUI
from ui import app
from version import v
print("""                                                                                                                 
                                                                                                                 
KKKKKKKKK    KKKKKKK                          tttt                                                               
K:::::::K    K:::::K                       ttt:::t                                                               
K:::::::K    K:::::K                       t:::::t                                                               
K:::::::K   K::::::K                       t:::::t                                                               
KK::::::K  K:::::KKK  aaaaaaaaaaaaa  ttttttt:::::ttttttt      aaaaaaaaaaaaa  nnnn  nnnnnnnn      aaaaaaaaaaaaa   
  K:::::K K:::::K     a::::::::::::a t:::::::::::::::::t      a::::::::::::a n:::nn::::::::nn    a::::::::::::a  
  K::::::K:::::K      aaaaaaaaa:::::at:::::::::::::::::t      aaaaaaaaa:::::an::::::::::::::nn   aaaaaaaaa:::::a 
  K:::::::::::K                a::::atttttt:::::::tttttt               a::::ann:::::::::::::::n           a::::a 
  K:::::::::::K         aaaaaaa:::::a      t:::::t              aaaaaaa:::::a  n:::::nnnn:::::n    aaaaaaa:::::a 
  K::::::K:::::K      aa::::::::::::a      t:::::t            aa::::::::::::a  n::::n    n::::n  aa::::::::::::a 
  K:::::K K:::::K    a::::aaaa::::::a      t:::::t           a::::aaaa::::::a  n::::n    n::::n a::::aaaa::::::a 
KK::::::K  K:::::KKKa::::a    a:::::a      t:::::t    tttttta::::a    a:::::a  n::::n    n::::na::::a    a:::::a 
K:::::::K   K::::::Ka::::a    a:::::a      t::::::tttt:::::ta::::a    a:::::a  n::::n    n::::na::::a    a:::::a 
K:::::::K    K:::::Ka:::::aaaa::::::a      tt::::::::::::::ta:::::aaaa::::::a  n::::n    n::::na:::::aaaa::::::a 
K:::::::K    K:::::K a::::::::::aa:::a       tt:::::::::::tt a::::::::::aa:::a n::::n    n::::n a::::::::::aa:::a
KKKKKKKKK    KKKKKKK  aaaaaaaaaa  aaaa         ttttttttttt    aaaaaaaaaa  aaaa nnnnnn    nnnnnn  aaaaaaaaaa  aaaa                                                                                                                                                                                                                                                                                                                            
""")
print("Development copy")
print("Distributed under the GNU AGPL 3.0 License")
print("Version: " + v)  
print("Credit to: SpiritDude for Print3R CLI tool")




FlaskUI(server="flask", app=app, extra_flags=["--class=Katana"]).run()
