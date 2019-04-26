#!/usr/bin/env python  
  
import wx  
import wx.lib.buttons as buttons  
  
  
class GenericButtonFrame(wx.Frame):  
    def __init__(self):  
        wx.Frame.__init__(self, None, -1, 'Generic Button Example',size=(500, 350))  
        panel = wx.Panel(self, -1)  
          
        sizer = wx.GridSizer(4, 3, 20, 20)  
        b = wx.Button(panel, -1, 'A wx.Button')  
        b.SetDefault()  
        sizer.Add(b)  
          
        b = wx.Button(panel, -1, 'non-default wx.Button')  
        sizer.Add(b)  
        sizer.Add((10, 10))  
          
        b = buttons.GenButton(panel, -1, 'Generic Button')  
        sizer.Add(b)  
  
        b = buttons.GenButton(panel, -1, 'disabled Generic')# invalid generic button  
        b.Enable(False)  
        sizer.Add(b)  
           
        b = buttons.GenButton(panel, -1, 'bigger')# a button with a customer size and color  
        b.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD, False))  
        b.SetBezelWidth(5)  
        b.SetBackgroundColour('Navy')  
        b.SetForegroundColour('white')  
        b.SetToolTipString('This is a BIG button…')  
        sizer.Add(b)  
           
        bmp = wx.Image('bitmap.ico', wx.BITMAP_TYPE_ANY).ConvertToBitmap()  
        b = buttons.GenBitmapButton(panel, -1, bmp)# generic bit button  
        sizer.Add(b)  
           
        b = buttons.GenBitmapToggleButton(panel, -1, bmp)# generic bit toggle button  
        sizer.Add(b)  
           
        b = buttons.GenBitmapTextButton(panel, -1, bmp, 'Bitmapped Text',  
                                        size=(175, 75))# bit text button  
        b.SetUseFocusIndicator(False)  
        sizer.Add(b)  
           
        b = buttons.GenToggleButton(panel, -1, 'Toggle Button')# generic toggle button  
        sizer.Add(b)  
        
        panel.SetSizer(sizer)  
        
          
if __name__=='__main__':  
    app = wx.PySimpleApp()  
    frame = GenericButtonFrame() 
    frame.Center() 
    frame.Show()  
    app.MainLoop()  