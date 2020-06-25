from numpy import *
import utilityFunctions as utilityFunctions
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from functions import *
from roofBuilder import *

class Pagoda_builder:
    def __init__(self, level, x, y, z,tree_ID,tree_data,wood_ID,wood_data,roof_ID):
        self.level = level
        self.x = x
        self.y = y
        self.z = z
        self.tree_ID = tree_ID
        self.tree_data = tree_data
        self.wood_ID = wood_ID
        self.wood_data = wood_data
        self.roof_ID = roof_ID

    def build(self):
        lv = self.level
        x = self.x
        y = self.y
        z = self.z
        t_ID =self.tree_ID
        t_data =self.tree_data
        w_ID = self.wood_ID
        w_data = self.wood_data
        r_ID = self.roof_ID
        d =[19, 16, 13, 10, 7, 4]   #depth size
        y_height = [0, 4, 8, 12, 16]  #height 

        def wall1st(lv,x,y,z,d):
            for i in range(d):
                for j in range(5):
                    if (i%3==0):
                        setBlock(lv, x, y+j, z+i, t_ID,t_data)
                        setBlock(lv, x+d-1, y+j, z+i, t_ID,t_data)
                        setBlock(lv, x+i, y+j, z, t_ID,t_data)
                        setBlock(lv, x+i, y+j, z+d-1, t_ID,t_data)
                    else:
                        setBlock(lv, x, y+j, z+i, w_ID,w_data)
                        setBlock(lv, x+d-1, y+j, z+i, w_ID,w_data)
                        setBlock(lv, x+i, y+j, z, w_ID,w_data)
                        setBlock(lv, x+i, y+j, z+d-1, w_ID,w_data)
                    if j==6-1:
                        setBlock(lv, x, y+j, z+i, t_ID,t_data)
                        setBlock(lv, x+d-1, y+j, z+i, t_ID,t_data)
                        setBlock(lv, x+i, y+j, z, t_ID,t_data)
                        setBlock(lv, x+i, y+j, z+d-1, t_ID,t_data)
            for i in range(7,12):
                for j in range(5):
                    setBlock(lv, x, y+j, z+i, 0, 0)
                    setBlock(lv, x+d-1, y+j, z+i, 0, 0)
                    setBlock(lv, x+i, y+j, z, 0, 0)
                    setBlock(lv, x+i, y+j, z+d-1, 0, 0)


        def wall(lv,x,y,z,d):
            for i in range(d):
                for j in range(5):
                    if (i%3==0):
                        setBlock(lv, x, y+j, z+i, t_ID,t_data)
                        setBlock(lv, x+d-1, y+j, z+i, t_ID,t_data)
                        setBlock(lv, x+i, y+j, z, t_ID,t_data)
                        setBlock(lv, x+i, y+j, z+d-1, t_ID,t_data)
                    else:
                        setBlock(lv, x, y+j, z+i, w_ID,w_data)
                        setBlock(lv, x+d-1, y+j, z+i, w_ID,w_data)
                        setBlock(lv, x+i, y+j, z, w_ID,w_data)
                        setBlock(lv, x+i, y+j, z+d-1, w_ID,w_data)
            for i in range(-1,d+1):
                setBlock(lv, x-1, y+1, z+i, 191, 0)
                setBlock(lv, x+d, y+1, z+i, 191, 0)
                setBlock(lv, x+i, y+1, z-1, 191, 0)
                setBlock(lv, x+i, y+1, z+d, 191, 0)
                setBlock(lv, x-1, y, z+i, 164, 8)
                setBlock(lv, x+d, y, z+i, 164, 5)
                setBlock(lv, x+i, y, z-1, 164, 6)
                setBlock(lv, x+i, y, z+d, 164, 7)
            
        
        def floor(lv,x,y,z,d):
            for i in range(1,d+3):
                for j in range(1,d+3):
                    setBlock(lv, x+i, y, z+j, 98, 0)#rstone
            for k in range(0,5):
                setBlock(lv, x+d/2+k, y, z, 109, 0)
                setBlock(lv, x+d/2+k, y, z+d+3, 109, 0)
                setBlock(lv, x, y, z+d/2+k, 109, 0)
                setBlock(lv, x+d+3, y, z+d/2+k, 109, 0)
        
        floor(lv,x,y,z,d[0])

        x+=2
        y+=1
        z+=2
        for i in range(5):
            if i==0:
                wall1st(lv, x + (d[0]/2-d[i]/2), y+y_height[i],  z + (d[0]/2-d[i]/2), d[i])
                roof_builder = RoofBuilder(lv, x + (d[0]/2-d[i+1]/2), z + (d[0]/2-d[i+1]/2), d[i+1], y+y_height[i]+5-1, 0, 1, t_ID,t_data,w_ID,w_data, r_ID)
                roof_builder.build()
            else:
                wall(lv, x + (d[0]/2-d[i]/2), y+y_height[i],  z + (d[0]/2-d[i]/2), d[i])
                roof_builder = RoofBuilder(lv, x + (d[0]/2-d[i+1]/2), z + (d[0]/2-d[i+1]/2), d[i+1], y+y_height[i]+5-1, 0, 1, t_ID,t_data,w_ID,w_data, r_ID)
                roof_builder.build()