import cv2 , pandas
import numpy

image1 = numpy.zeros((700,1000,3))


#cv2.imwrite("image1.jpg",image1)
cv2.imshow("devesh",image1)
cv2.waitKey()
cv2.destroyAllWindows()

#image1[100:400 , 100:120]=[0,0,0]
#image1[150:400 , 100:110]=[0,0,0]
cv2.rectangle(image1, (250, 300), (350, 370), (255,0,0), -2)
cv2.rectangle(image1, (250, 300), (350, 370), (0,0,255), 2)
cv2.rectangle(image1, (130, 300), (170, 396), (255,0,0), -2)
cv2.rectangle(image1, (130, 300), (170, 396), (0,0,255), 2)
cv2.circle(image1,(950,50),30,[255,255,255],-1)
cv2.circle(image1,(150,260),15,[255,0,0],-1)
cv2.circle(image1,(150,260),15,[0,0,255],2)

image1[300:370 , 300:304]=[0,0,255]
image1[330:334 , 250:350]=[0,0,255]

cv2.rectangle(image1,(0,330),(98,700),(0,255,0),-2)
cv2.rectangle(image1,(406,330),(1000,700),(0,255,0),-2)
cv2.rectangle(image1,(98,406),(1000,700),(0,255,0),-2)

cv2.line(image1, (300,50), (0,200), [0,255,255],2)
cv2.line(image1, (300,50), (520,200), [0,255,255],2)
cv2.line(image1, (700,50), (400,120), [0,255,255],2)
cv2.line(image1, (700,50), (1000,200), [0,255,255],2)

image1[250:400 , 100:104]=[0,0,255] #first vertical line
image1[400:404 , 100:400]=[0,0,255] #botom 3ed horizontal line
image1[250:404 , 200:204]=[0,0,255] #second vertical line
image1[250:404 , 400:404]=[0,0,255] #thired vertical line
image1[200:204 , 150:350]=[0,0,255] #top 1st horizontal line
image1[260:264 , 215:415]=[0,0,255] #midil 2nd horizontal line


image1[214:218 , 164:364]=[0,0,255] #top M1st horizontal line
image1[228:232 , 176:376]=[0,0,255] #top M2st horizontal line
image1[242:246 , 192:392]=[0,0,255] #top M3st horizontal line


#this is for first (1st) digonal line ----------------------------------------------
line1      = 200
line1_2    = 204
c_line1    = 150
c_line1_2  = 154

while True:
    if  ( line1 == 272 ) and (c_line1 == 78): 
        break
        
    else:
        image1[line1:line1_2 , c_line1:c_line1_2] =[0,0,255]
        
    line1      = line1+4
    line1_2    = line1_2+4
    c_line1    = c_line1-4
    c_line1_2  = c_line1_2-4


#this is for second (2nd) digonal line ----------------------------------------------
line2      = 200
line2_2    = 204
c_line2    = 150
c_line2_2  = 154
while True:
    if  ( line2 == 264 ) and (c_line2 == 214): 
        break
        
    else:
        image1[line2:line2_2 , c_line2:c_line2_2] =[0,0,255]
        
    line2     = line2+4
    line2_2   = line2_2+4
    c_line2   = c_line2+4
    c_line2_2 = c_line2_2+4  
    
    
    
#this is for second (2nd) digonal line ----------------------------------------------
xline2     = 200
xline2_2    = 204
xc_line2    = 150
xc_line2_2  = 154
while True:
    if  ( xline2 == 264 ) and (xc_line2 == 214): 
        break
        
    else:
        image1[xline2:xline2_2 , xc_line2:xc_line2_2] =[0,0,255]
        
    xline2     = xline2+4
    xline2_2   = xline2_2+4
    xc_line2   = xc_line2+4
    xc_line2_2 = xc_line2_2+4  

#this is for last (3ed) digonal line ----------------------------------------------
line3      = 200
line3_2    = 204
c_line3    = 350
c_line3_2  = 354
while True:
    if  ( line3 == 264 ) and (c_line3 == 414): 
        break
        
    else:
        image1[line3:line3_2 , c_line3:c_line3_2] =[0,0,255]
        
    line3      = line3+4
    line3_2    = line3_2+4
    c_line3    = c_line3+4
    c_line3_2  = c_line3_2+4  
    
    
#this is for second (2nd) M__digonal line ----------------------------------------------
xc_line2    = 150 
xc_line2_2  = 154 
for i in range(0,3):
    xline2      = 200
    xline2_2    = 204
    while True:
        if   xline2 == 264 : 
            break

        else:
            image1[xline2:xline2_2 , xc_line2:xc_line2_2] =[0,0,255]

        xline2     = xline2+4
        xline2_2   = xline2_2+4
        xc_line2   = xc_line2+4
        xc_line2_2 = xc_line2_2+4 
        
    xc_line2    +=  2
    xc_line2_2  +=  2

    
#for showing the image/photo....................................................
#cv2.imwrite("image1.jpg",image1)
cv2.imshow("devesh",image1)
cv2.waitKey()
cv2.destroyAllWindows()
