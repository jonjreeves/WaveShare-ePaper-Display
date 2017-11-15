#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 19:14:40 2017
"""


import serial

class Display:
    def __init__(self):
        self.baudrate=115200
        self.comPort="/dev/ttyUSB1"
        self.connection=None
    
    def setBaudRate(self, rate):
        self.baudrate=rate
    
    def setComPort(self,port):
        self.comPort=port
    
    def connect(self):
        self.connection = serial.Serial(port=self.comPort, baudrate=self.baudrate, timeout=1)
    	
    def calcParity(self,_bytearray):
        parity = 0x00
        for _byte in _bytearray:
            parity=parity^_byte
       # _bytearray.append(parity)
        #return b''.join(bytes)
        return bytes([parity])
    
    def send(self,cmdType,cmdParam):
        if self.connection == None:
            print(">> EPD not connected. Try epd_connect()")
        else:
            frameHeader=b'\xA5'
            frameEnd=b'\xCC\x33\xC3\x3C'

            if cmdParam==None:
                frameLength=bytearray([0x09])
                frameLength=bytes(1)+frameLength #frame length is always length of 2
                frameLength=frameLength[-2:]
                frame=bytearray(frameHeader+frameLength+cmdType+frameEnd)
            else:
                frameLength=bytearray([len(cmdParam)+0x09])
                frameLength=bytes(1)+frameLength #frame length is always length of 2
                frameLength=frameLength[-2:]
                frame=bytearray(frameHeader+frameLength+cmdType+cmdParam+frameEnd)
            

            parity=self.calcParity(frame)
            frame+=parity
            self.connection.write(frame)
            self.connection.flushInput()
            
    def print(self,x,y,text):
        cmdType=b'\x30'
        textBytes=bytearray(text,'ascii')+bytes(1)
        xBytes=x.to_bytes(2,byteorder='big')
        yBytes=y.to_bytes(2,byteorder='big')
        cmdParm=xBytes[-2:]+yBytes[-2:]+textBytes
        self.send(cmdType,cmdParm)
        
    def drawBMP(self,x,y,name):
        cmdType=b'\x70'
        textBytes=bytearray(name,'ascii')+bytes(1)
        xBytes=x.to_bytes(2,byteorder='big')
        yBytes=y.to_bytes(2,byteorder='big')
        cmdParm=xBytes[-2:]+yBytes[-2:]+textBytes
        self.send(cmdType,cmdParm)
        
    def setFontSize(self,size):
        cmdType=b'\x1E'
        if size==32:
            cmdParam=b'\x01'
        elif size==48:
            cmdParam=b'\x02'
        elif size==68:
            cmdParam=b'\x03'
        else:
            cmdParam=b'\x02'
        self.send(cmdType,cmdParam)
        
    def setRotation(self,angle):
        cmdType=b'\x0D'
        if angle==0:
            cmdParam=b'\x00'
        elif angle==180:
            cmdParam=b'\x01'
        else:
            cmdParam=b'\x00'
        self.send(cmdType,cmdParam)
        
    def setStorage(self,storageStr):
        cmdType=b'\x07'
        if storageStr=='NAND':
            cmdParam=b'\x00'
        elif storageStr=='SD':
            cmdParam=b'\x01'
        else:
            cmdParam=b'\x00'
        self.send(cmdType,cmdParam)
        
    def update(self):
        self.send(b'\x0A',None)
        
    def sleep(self):
        self.send(b'\x08',None)
        
    def clear(self):
        self.send(b'\x2E',None)
        
    def drawLine(self,x0,y0,x1,y1):
        cmdType=b'\x22'
        x0Bytes=x0.to_bytes(2,byteorder='big')
        y0Bytes=y0.to_bytes(2,byteorder='big')
        x1Bytes=x1.to_bytes(2,byteorder='big')
        y1Bytes=y1.to_bytes(2,byteorder='big')
        cmdParams=x0Bytes+y0Bytes+x1Bytes+y1Bytes
        self.send(cmdType,cmdParams)
        
    def drawFillRect(self,x0,y0,x1,y1):
        cmdType=b'\x24'
        x0Bytes=x0.to_bytes(2,byteorder='big')
        y0Bytes=y0.to_bytes(2,byteorder='big')
        x1Bytes=x1.to_bytes(2,byteorder='big')
        y1Bytes=y1.to_bytes(2,byteorder='big')
        cmdParams=x0Bytes+y0Bytes+x1Bytes+y1Bytes
        self.send(cmdType,cmdParams)
        
    def drawRect(self,x0,y0,x1,y1):
        cmdType=b'\x25'
        x0Bytes=x0.to_bytes(2,byteorder='big')
        y0Bytes=y0.to_bytes(2,byteorder='big')
        x1Bytes=x1.to_bytes(2,byteorder='big')
        y1Bytes=y1.to_bytes(2,byteorder='big')
        cmdParams=x0Bytes+y0Bytes+x1Bytes+y1Bytes
        self.send(cmdType,cmdParams)
        
    def drawCir(self,x0,y0,r):
        cmdType=b'\x26'
        x0Bytes=x0.to_bytes(2,byteorder='big')
        y0Bytes=y0.to_bytes(2,byteorder='big')
        rBytes=r.to_bytes(2,byteorder='big')
        cmdParams=x0Bytes+y0Bytes+rBytes
        self.send(cmdType,cmdParams)
        
    def drawFillCir(self,x0,y0,r):
        cmdType=b'\x27'
        x0Bytes=x0.to_bytes(2,byteorder='big')
        y0Bytes=y0.to_bytes(2,byteorder='big')
        rBytes=r.to_bytes(2,byteorder='big')
        cmdParams=x0Bytes+y0Bytes+rBytes
        self.send(cmdType,cmdParams)
        
    def drawTri(self,x0,y0,x1,y1,x2,y2):
        cmdType=b'\x28'
        x0Bytes=x0.to_bytes(2,byteorder='big')
        y0Bytes=y0.to_bytes(2,byteorder='big')
        x1Bytes=x1.to_bytes(2,byteorder='big')
        y1Bytes=y1.to_bytes(2,byteorder='big')
        x2Bytes=x2.to_bytes(2,byteorder='big')
        y2Bytes=y2.to_bytes(2,byteorder='big')
        cmdParams=x0Bytes+y0Bytes+x1Bytes+y1Bytes+x2Bytes+y2Bytes
        self.send(cmdType,cmdParams)
        
    def drawFillTri(self,x0,y0,x1,y1,x2,y2):
        cmdType=b'\x29'
        x0Bytes=x0.to_bytes(2,byteorder='big')
        y0Bytes=y0.to_bytes(2,byteorder='big')
        x1Bytes=x1.to_bytes(2,byteorder='big')
        y1Bytes=y1.to_bytes(2,byteorder='big')
        x2Bytes=x2.to_bytes(2,byteorder='big')
        y2Bytes=y2.to_bytes(2,byteorder='big')
        cmdParams=x0Bytes+y0Bytes+x1Bytes+y1Bytes+x2Bytes+y2Bytes
        self.send(cmdType,cmdParams)
        




if __name__=="__main__":
    display=Display()
    display.connect()
    display.clear()
    display.drawBMP(0,0,'PIC7.BMP')
    display.update()