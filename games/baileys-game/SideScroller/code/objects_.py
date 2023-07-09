from bullets import Bullet_mat
from stats import *
from guns import Gun

tags = {
    'M':'smg',
    'S':'shotgun',
    'R':'rifle',
    'B':'banana_gun'
}


guns = {
    'smg':[Gun,[(3*scale,4*scale),(9*scale,1*scale),0.1,5,16,1.5,1,'light_ammo'],Bullet_mat(lifetime = 5,dmg=11,speed=6*scale)],#smg
    'shotgun':[Gun,[(3*scale,4*scale),(13*scale,1*scale),1,10,5,4,7,'shells'],Bullet_mat(lifetime=5,dmg=15,speed=6*scale)],#shotgun
    'rifle':[Gun,[(5*scale,4*scale),(14*scale,2*scale),0.25,1,20,2,1,'medium_ammo'],Bullet_mat(lifetime=5,dmg=20,speed=10*scale)],#rifle
    'banana_gun':[Gun,[(3*scale,8*scale),(19*scale,6*scale),0.15,1,1,1,1,'rockets'],Bullet_mat(lifetime=11,dmg=80,speed=5*scale,explode=True)]#banana gun
}


# gunss = {
#     'smg':
#     'sniper':0,
#     'rifle': Bullet_mat(lifetime=5,dmg=20,speed=10*scale,img=bullet),
#     'bangun':Bullet_mat(lifetime=11,dmg=40,speed=5*scale,img=banbull),
#     'shotgun':Bullet_mat(lifetime=5,dmg=15,speed=6*scale,img=pellet)
# }