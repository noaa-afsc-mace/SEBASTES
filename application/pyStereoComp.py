 
''' attempt at writing a triangulation function to mimic matlab camera calibration toolbox'''



from scipy.io import matlab
from math import *
from numpy import *
import cv2
import traceback,  sys


class pyStereoComp(object):

    def __init__(self):
        self.calData={}
        self.mode='matlab'# teh default

    def importCalData(self, fname):
        if self.mode=='matlab':
            try:
                self.calData=matlab.loadmat(fname)
                #--- Rotation matrix corresponding to the rigid motion between left and right cameras:
                if not 'R' in self.calData:
                    out=cv2.Rodrigues(self.calData['om'])
                    self.calData.update({'R':out[0]})

                self.calData.update({'cameraMatrixL':array([[self.calData['fc_left'][0][0], 0., self.calData['cc_left'][0][0]],
                                                                                    [0.,self.calData['fc_left'][1][0],  self.calData['cc_left'][1][0]], 
                                                                                    [0., 0., 1.]])})
                self.calData.update({'cameraMatrixR':array([[self.calData['fc_right'][0][0], 0., self.calData['cc_right'][0][0]],
                                                                                    [0.,self.calData['fc_right'][1][0],  self.calData['cc_right'][1][0]], 
                                                                                    [0., 0., 1.]])})
                self.calData['distCoeffsL']=self.calData['kc_left']
                self.calData['distCoeffsR']=self.calData['kc_right']
                #self.calData['T']=self.calData['T'].T
                return True,  self.calData
            except:
                msg=self.showError()
                return False,  msg
                
        elif self.mode=='openCV':
            try:
                npzfileData = load(fname)
                self.calData={'cameraMatrixL':npzfileData['cameraMatrixL'],'distCoeffsL':npzfileData['distCoeffsL'], 
                'kc_left':npzfileData['distCoeffsL'][0], 'kc_right':npzfileData['distCoeffsR'][0],
               'cameraMatrixR':npzfileData['cameraMatrixR'],'distCoeffsR':npzfileData['distCoeffsR'], 
                    'R':npzfileData['R'], 'T':npzfileData['T'] }
                if 'F' in npzfileData:
                    self.calData.update({'F':npzfileData['F']})
                R=self.calData['R']

                calmat=npzfileData['cameraMatrixL']
                self.calData.update({'fc_left':array([[calmat[0,0]],[calmat[1,1]]])})
                self.calData.update({'cc_left':array([[calmat[0,2]],[calmat[1,2]]])})
                self.calData.update({'alpha_c_left':array([[calmat[0,1]]])})

                calmat=npzfileData['cameraMatrixR']
                self.calData.update({'fc_right':array([[calmat[0,0]],[calmat[1,1]]])})
                self.calData.update({'cc_right':array([[calmat[0,2]],[calmat[1,2]]])})
                self.calData.update({'alpha_c_right':array([[calmat[0,1]]])})

                return True,  self.calData
            except:
                msg=self.showError()
                return False,  msg
        elif self.mode=='yaml':
            try:
                import yaml
                f= open(fname, "r")
                    # Load the YAML data using yaml.safe_load() for security
                p = yaml.safe_load(f)
                yaml_data=yaml.safe_load(p)
                self.calData={'kc_left':array([[yaml_data['Camera1']['Intrinsic']['radial_distortion']['k1']], 
                [yaml_data['Camera1']['Intrinsic']['radial_distortion']['k2']], 
                [yaml_data['Camera1']['Intrinsic']['tangential_distortion']['p1']], 
                [yaml_data['Camera1']['Intrinsic']['tangential_distortion']['p2']], 
                [yaml_data['Camera1']['Intrinsic']['radial_distortion']['k3']]]), 
                'kc_right':array([[yaml_data['Camera2']['Intrinsic']['radial_distortion']['k1']], 
                [yaml_data['Camera2']['Intrinsic']['radial_distortion']['k2']], 
                [yaml_data['Camera2']['Intrinsic']['tangential_distortion']['p1']], 
                [yaml_data['Camera2']['Intrinsic']['tangential_distortion']['p2']], 
                [yaml_data['Camera2']['Intrinsic']['radial_distortion']['k3']]]),
                'cc_left':array([[yaml_data['Camera1']['Intrinsic']['principal_point']['h']], [yaml_data['Camera1']['Intrinsic']['principal_point']['v']]]), 
                'cc_right':array([[yaml_data['Camera2']['Intrinsic']['principal_point']['h']], [yaml_data['Camera2']['Intrinsic']['principal_point']['v']]]), 
                'fc_left':array([[yaml_data['Camera1']['Intrinsic']['focal_length']['h']], [ yaml_data['Camera1']['Intrinsic']['focal_length']['v']]]), 
                'fc_right':array([[yaml_data['Camera2']['Intrinsic']['focal_length']['h']], [ yaml_data['Camera2']['Intrinsic']['focal_length']['v']]]), 
                'alpha_c_left':array([[0]]), 'alpha_c_right':array([[0]])}
                if yaml_data['Camera1']['Extrinsic']['R']['r2c1']==0.:# we have a non-seagis situation here, single meaningful rotation matrix
                    self.calData.update({'R':array([[yaml_data['Camera2']['Extrinsic']['R']['r1c1'], yaml_data['Camera2']['Extrinsic']['R']['r1c2'], yaml_data['Camera2']['Extrinsic']['R']['r1c3']],
                    [yaml_data['Camera2']['Extrinsic']['R']['r2c1'], yaml_data['Camera2']['Extrinsic']['R']['r2c2'], yaml_data['Camera2']['Extrinsic']['R']['r2c3']],
                    [yaml_data['Camera2']['Extrinsic']['R']['r3c1'], yaml_data['Camera2']['Extrinsic']['R']['r3c2'], yaml_data['Camera2']['Extrinsic']['R']['r3c3']]]),
                    'T':array([[yaml_data['Camera2']['Extrinsic']['T']['t1'], yaml_data['Camera2']['Extrinsic']['T']['t2'], yaml_data['Camera2']['Extrinsic']['T']['t3']]]).T})
                else: # this is a seagis cal
                    R1=array([[yaml_data['Camera1']['Extrinsic']['R']['r1c1'], yaml_data['Camera1']['Extrinsic']['R']['r1c2'], yaml_data['Camera1']['Extrinsic']['R']['r1c3']],
                    [yaml_data['Camera1']['Extrinsic']['R']['r2c1'], yaml_data['Camera1']['Extrinsic']['R']['r2c2'], yaml_data['Camera1']['Extrinsic']['R']['r2c3']],
                    [yaml_data['Camera1']['Extrinsic']['R']['r3c1'], yaml_data['Camera1']['Extrinsic']['R']['r3c2'], yaml_data['Camera1']['Extrinsic']['R']['r3c3']]])
                    R2=array([[yaml_data['Camera2']['Extrinsic']['R']['r1c1'], yaml_data['Camera2']['Extrinsic']['R']['r1c2'], yaml_data['Camera2']['Extrinsic']['R']['r1c3']],
                    [yaml_data['Camera2']['Extrinsic']['R']['r2c1'], yaml_data['Camera2']['Extrinsic']['R']['r2c2'], yaml_data['Camera2']['Extrinsic']['R']['r2c3']],
                    [yaml_data['Camera2']['Extrinsic']['R']['r3c1'], yaml_data['Camera2']['Extrinsic']['R']['r3c2'], yaml_data['Camera2']['Extrinsic']['R']['r3c3']]])
                    T1=array([[yaml_data['Camera1']['Extrinsic']['T']['t1'], yaml_data['Camera1']['Extrinsic']['T']['t2'], yaml_data['Camera1']['Extrinsic']['T']['t3']]])
                    T2=array([[yaml_data['Camera2']['Extrinsic']['T']['t1'], yaml_data['Camera2']['Extrinsic']['T']['t2'], yaml_data['Camera2']['Extrinsic']['T']['t3']]])
                    R=dot(R2.T, R1)
                    T=dot(R2.T, T1.T-T2.T)
                    self.calData.update({'R':R, 'T':T})
                    
                    
                self.calData.update({'cameraMatrixL':array([[self.calData['fc_left'][0][0], 0., self.calData['cc_left'][0][0]],
                                                                                    [0.,self.calData['fc_left'][1][0],  self.calData['cc_left'][1][0]], 
                                                                                    [0., 0., 1.]])})
                self.calData.update({'cameraMatrixR':array([[self.calData['fc_right'][0][0], 0., self.calData['cc_right'][0][0]],
                                                                                    [0.,self.calData['fc_right'][1][0],  self.calData['cc_right'][1][0]], 
                                                                                    [0., 0., 1.]])})
                self.calData['distCoeffsL']=self.calData['kc_left']
                self.calData['distCoeffsR']=self.calData['kc_right']
                return True,  self.calData
            except:
                msg=self.showError()
                return False,  msg
            
        else:
            return False,  'mode unrecognized'
    
    def triangulatePoint(self, xL, xR):
        hxL=zeros((xL.shape[1], 1, 2))
        hxR=zeros((xL.shape[1], 1, 2))
        for i in range(xL.shape[1]):
            hxL[i, 0, 0]=xL[0, i]
            hxL[i, 0, 1]=xL[1, i]
            hxR[i, 0, 0]=xR[0, i]
            hxR[i, 0, 1]=xR[1, i]
        PL =  hstack((eye(3).astype('float32') ,zeros((3, 1)).astype('float32')))
        PR =  hstack((self.calData['R'] ,self.calData['T']))
        imgptsL=cv2.undistortPoints(hxL,self.calData['cameraMatrixL'], self.calData['distCoeffsL'])
        imgptsR=cv2.undistortPoints(hxR, self.calData['cameraMatrixR'], self.calData['distCoeffsR'])
        XL=cv2.triangulatePoints(PL, PR, imgptsL,imgptsR)
        XL/=XL[3]
        XL=XL[0:3]
        T_vect = tile(self.calData['T'], (1, xL.shape[1]))
        XR = dot(self.calData['R'], XL) + T_vect
        return (XL, XR)

    def computeMatch(self,  im1,  im2,  point):
        if  len(im1.shape)>2:
            gray_left = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
        else:
            gray_left = im1
            
        if  len(im2.shape)>2:
            gray_right = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
        else:
            gray_right = im2
                  

        #single point match
        block=80
        if point[0, 0]<block or point[0, 1]<block:# too close tot eh edge
            return False,  zeros((1, 2)),  'Point too close to the image edge'
        #find point
        kernel_fish=gray_left[int(point[0, 1]-block):int(point[0, 1]+block),int(point[0, 0]-block):int(point[0, 0]+block)]
        im_strip=gray_right[max([int(point[0, 1]-block*2), 0]):max([int(point[0, 1]+block*2), kernel_fish.shape[0]]),:]
        try:
            res = cv2.matchTemplate(im_strip,kernel_fish,eval('cv2.TM_CCOEFF_NORMED'))
        except:
            return False,  zeros((1, 2)), 'pyOpenCV matchTemplate function error error'
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        top_left_kernel=(int(point[0, 0]), int(point[0, 1]-block))
        dx=array([point[0, 0]-top_left_kernel[0], point[0, 1]-top_left_kernel[1]])
        top_left_kernel_fit=(max_loc[0]+block,int(point[0, 1]-block*2)+ max_loc[1])
        point_r=zeros((1, 2))
        point_r[0, :]=array([top_left_kernel_fit[0]+dx[0], top_left_kernel_fit[1]+dx[1]])
        return True,  point_r,  max_val

    
    def projectPoint(self, X, I):
        if I=='L':
            xp, J=cv2.projectPoints(X.T,  eye(3), zeros((3, 1)),self.calData['cameraMatrixL'], self.calData['distCoeffsL'])
        elif I=='R':
            xp, J=cv2.projectPoints(X.T,  eye(3), zeros((3, 1)), self.calData['cameraMatrixR'], self.calData['distCoeffsR'])
        if xp.shape[0]<2:
            xp=xp[0].T
        else:
            xp=reshape(xp,(2,2)).T
        return xp
            
    def computeError(self,xL,xpL,xR,xpR):

        e1 = (xL[0, :]-xpL[0,:])**2
        e2 = (xL[1,:]-xpL[1,:])**2
        e3 = (xR[0,:]-xpR[0,:])**2
        e4 = (xR[1,:]-xpR[1,:])**2

        eL = sqrt(e1+e2)
        eR = sqrt(e3+e4) 

        error = sum(eL+eR)/2      
        
        return error
        
    def showError(self):
        t=traceback.format_exception(*sys.exc_info())
        txt=''
        for line in t:
            txt=txt+line+'\n'
            #self.emit(SIGNAL("message"), self,line, 'error')
        print(txt)
        return txt
#    import pyStereoComp
#    x=pyStereoComp.pyStereoComp()
#    x.importMatlabself.calData('10052010_8mm_calibration')
#    import numpy as ny
#    xL=array([[826,1230],[915,1044]])
#    xR=array([[77,439],[908,1034]])
#    (XL, XR)=x.triangulatePoint(xL,xR)
#    pass
