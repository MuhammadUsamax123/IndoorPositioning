<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1366</width>
    <height>765</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QFrame" name="frame">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>1366</width>
      <height>768</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #ffffff</string>
    </property>
    <property name="frameShape">
     <enum>QFrame::StyledPanel</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <widget class="QLabel" name="label">
     <property name="geometry">
      <rect>
       <x>0</x>
       <y>0</y>
       <width>310</width>
       <height>768</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-image: url(null);
background-color:#2F3C71;</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QLabel" name="label_2">
     <property name="geometry">
      <rect>
       <x>0</x>
       <y>0</y>
       <width>1366</width>
       <height>44</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-image: url(null);
background-color:#222222;</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QPushButton" name="navViewPunishment">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>587</y>
       <width>290</width>
       <height>44</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Segoe UI</family>
       <pointsize>11</pointsize>
      </font>
     </property>
     <property name="cursor">
      <cursorShape>PointingHandCursor</cursorShape>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton 
{
    text-align: left;
    color: #ffffff;
    background-color:#2F3C71;
    border-width: 1px;
    border-color: #2F3C71;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
    min-width: 40px;
}

QPushButton:hover
{
    background-color:#4154A0;
}
QPushButton:pressed
{
    background-color: #384889;
 	border-width: 3px;
    border-color: #5C70BC;
    border-style: solid;
    border-radius: 6;

}</string>
     </property>
     <property name="text">
      <string>Punishment Book</string>
     </property>
     <property name="icon">
      <iconset resource="../IconResource.qrc">
       <normaloff>:/images/punishment.png</normaloff>:/images/punishment.png</iconset>
     </property>
     <property name="iconSize">
      <size>
       <width>25</width>
       <height>25</height>
      </size>
     </property>
     <property name="flat">
      <bool>false</bool>
     </property>
    </widget>
    <widget class="QPushButton" name="navViewImpKey">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>323</y>
       <width>290</width>
       <height>44</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Segoe UI</family>
       <pointsize>11</pointsize>
      </font>
     </property>
     <property name="cursor">
      <cursorShape>PointingHandCursor</cursorShape>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton 
{
    text-align: left;
    color: #ffffff;
    background-color:#2F3C71;
    border-width: 1px;
    border-color: #2F3C71;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
    min-width: 40px;
}

QPushButton:hover
{
    background-color:#4154A0;
}
QPushButton:pressed
{
    background-color: #384889;
 	border-width: 3px;
    border-color: #5C70BC;
    border-style: solid;
    border-radius: 6;

}</string>
     </property>
     <property name="text">
      <string>Important Key Book</string>
     </property>
     <property name="icon">
      <iconset resource="../IconResource.qrc">
       <normaloff>:/images/impKey.png</normaloff>:/images/impKey.png</iconset>
     </property>
     <property name="iconSize">
      <size>
       <width>25</width>
       <height>25</height>
      </size>
     </property>
     <property name="flat">
      <bool>false</bool>
     </property>
    </widget>
    <widget class="QPushButton" name="navViewGenKey">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>367</y>
       <width>290</width>
       <height>44</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Segoe UI</family>
       <pointsize>11</pointsize>
      </font>
     </property>
     <property name="cursor">
      <cursorShape>PointingHandCursor</cursorShape>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton 
{
    text-align: left;
    color: #ffffff;
    background-color:#2F3C71;
    border-width: 1px;
    border-color: #2F3C71;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
    min-width: 40px;
}

QPushButton:hover
{
    background-color:#4154A0;
}

QPushButton:pressed
{
    background-color: #384889;
 	border-width: 3px;
    border-color: #5C70BC;
    border-style: solid;
    border-radius: 6;

}</string>
     </property>
     <property name="text">
      <string>General Key Book</string>
     </property>
     <property name="icon">
      <iconset resource="../IconResource.qrc">
       <normaloff>:/images/genKey.png</normaloff>:/images/genKey.png</iconset>
     </property>
     <property name="iconSize">
      <size>
       <width>25</width>
       <height>25</height>
      </size>
     </property>
     <property name="flat">
      <bool>false</bool>
     </property>
    </widget>
    <widget class="QPushButton" name="navViewVisitor">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>411</y>
       <width>290</width>
       <height>44</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Segoe UI</family>
       <pointsize>11</pointsize>
      </font>
     </property>
     <property name="cursor">
      <cursorShape>PointingHandCursor</cursorShape>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton 
{
    text-align: left;
    color: #ffffff;
    background-color:#2F3C71;
    border-width: 1px;
    border-color: #2F3C71;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
    min-width: 40px;
}

QPushButton:hover
{
    background-color:#4154A0;
}

QPushButton:pressed
{
    background-color: #384889;
 	border-width: 3px;
    border-color: #5C70BC;
    border-style: solid;
    border-radius: 6;
}</string>
     </property>
     <property name="text">
      <string>Visitor Book</string>
     </property>
     <property name="icon">
      <iconset resource="../IconResource.qrc">
       <normaloff>:/images/visitor.png</normaloff>:/images/visitor.png</iconset>
     </property>
     <property name="iconSize">
      <size>
       <width>25</width>
       <height>25</height>
      </size>
     </property>
     <property name="flat">
      <bool>false</bool>
     </property>
    </widget>
    <widget class="QPushButton" name="navViewTransport">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>455</y>
       <width>290</width>
       <height>44</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Segoe UI</family>
       <pointsize>11</pointsize>
      </font>
     </property>
     <property name="cursor">
      <cursorShape>PointingHandCursor</cursorShape>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton 
{
    text-align: left;
    color: #ffffff;
    background-color:#2F3C71;
    border-width: 1px;
    border-color: #2F3C71;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
    min-width: 40px;
}

QPushButton:hover
{
    background-color:#4154A0;
}
QPushButton:pressed
{
    background-color: #384889;
 	border-width: 3px;
    border-color: #5C70BC;
    border-style: solid;
    border-radius: 6;

}</string>
     </property>
     <property name="text">
      <string>Transport Book</string>
     </property>
     <property name="icon">
      <iconset resource="../IconResource.qrc">
       <normaloff>:/images/transport.png</normaloff>:/images/transport.png</iconset>
     </property>
     <property name="iconSize">
      <size>
       <width>25</width>
       <height>25</height>
      </size>
     </property>
     <property name="flat">
      <bool>false</bool>
     </property>
    </widget>
    <widget class="QPushButton" name="navViewGangway">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>499</y>
       <width>290</width>
       <height>44</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Segoe UI</family>
       <pointsize>11</pointsize>
      </font>
     </property>
     <property name="cursor">
      <cursorShape>PointingHandCursor</cursorShape>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton 
{
    text-align: left;
    color: #ffffff;
    background-color:#2F3C71;
    border-width: 1px;
    border-color: #2F3C71;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
    min-width: 40px;
}

QPushButton:hover
{
    background-color:#4154A0;
}
QPushButton:pressed
{
    background-color: #384889;
 	border-width: 3px;
    border-color: #5C70BC;
    border-style: solid;
    border-radius: 6;

}</string>
     </property>
     <property name="text">
      <string>Gangway Book</string>
     </property>
     <property name="icon">
      <iconset resource="../IconResource.qrc">
       <normaloff>:/images/gangway.png</normaloff>:/images/gangway.png</iconset>
     </property>
     <property name="iconSize">
      <size>
       <width>25</width>
       <height>25</height>
      </size>
     </property>
     <property name="flat">
      <bool>false</bool>
     </property>
    </widget>
    <widget class="QPushButton" name="navViewDuty">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>543</y>
       <width>290</width>
       <height>44</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Segoe UI</family>
       <pointsize>11</pointsize>
      </font>
     </property>
     <property name="cursor">
      <cursorShape>PointingHandCursor</cursorShape>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton 
{
    text-align: left;
    color: #ffffff;
    background-color:#2F3C71;
    border-width: 1px;
    border-color: #2F3C71;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
    min-width: 40px;
}

QPushButton:hover
{
    background-color:#4154A0;
}
QPushButton:pressed
{
    background-color: #384889;
 	border-width: 3px;
    border-color: #5C70BC;
    border-style: solid;
    border-radius: 6;

}</string>
     </property>
     <property name="text">
      <string>Duty Book</string>
     </property>
     <property name="icon">
      <iconset resource="../IconResource.qrc">
       <normaloff>:/images/duty.png</normaloff>:/images/duty.png</iconset>
     </property>
     <property name="iconSize">
      <size>
       <width>25</width>
       <height>25</height>
      </size>
     </property>
     <property name="flat">
      <bool>false</bool>
     </property>
    </widget>
    <widget class="QPushButton" name="navViewNight">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>675</y>
       <width>290</width>
       <height>44</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Segoe UI</family>
       <pointsize>11</pointsize>
      </font>
     </property>
     <property name="cursor">
      <cursorShape>PointingHandCursor</cursorShape>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton 
{
    text-align: left;
    color: #ffffff;
    background-color:#2F3C71;
    border-width: 1px;
    border-color: #2F3C71;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
    min-width: 40px;
}

QPushButton:hover
{
    background-color:#4154A0;
}
QPushButton:pressed
{
    background-color: #384889;
 	border-width: 3px;
    border-color: #5C70BC;
    border-style: solid;
    border-radius: 6;

}</string>
     </property>
     <property name="text">
      <string>Night Round Book</string>
     </property>
     <property name="icon">
      <iconset resource="../IconResource.qrc">
       <normaloff>:/images/night.png</normaloff>:/images/night.png</iconset>
     </property>
     <property name="iconSize">
      <size>
       <width>25</width>
       <height>25</height>
      </size>
     </property>
     <property name="flat">
      <bool>false</bool>
     </property>
    </widget>
    <widget class="QLabel" name="label_4">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>272</y>
       <width>290</width>
       <height>2</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color:#4154A0;</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QPushButton" name="navViewMOB">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>91</y>
       <width>290</width>
       <height>44</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Segoe UI</family>
       <pointsize>11</pointsize>
      </font>
     </property>
     <property name="cursor">
      <cursorShape>PointingHandCursor</cursorShape>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton 
{
    text-align: left;
    color: #ffffff;
    background-color:#2F3C71;
    border-width: 1px;
    border-color: #2F3C71;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
    min-width: 40px;
}

QPushButton:hover
{
    background-color:#4154A0;
}
QPushButton:pressed
{
    background-color: #384889;
 	border-width: 3px;
    border-color: #5C70BC;
    border-style: solid;
    border-radius: 6;

}</string>
     </property>
     <property name="text">
      <string>Man Over Board</string>
     </property>
     <property name="icon">
      <iconset resource="../IconResource.qrc">
       <normaloff>:/images/mob.png</normaloff>:/images/mob.png</iconset>
     </property>
     <property name="iconSize">
      <size>
       <width>32</width>
       <height>32</height>
      </size>
     </property>
     <property name="flat">
      <bool>false</bool>
     </property>
    </widget>
    <widget class="QPushButton" name="navViewLocation">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>3</y>
       <width>290</width>
       <height>44</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Segoe UI</family>
       <pointsize>11</pointsize>
      </font>
     </property>
     <property name="cursor">
      <cursorShape>PointingHandCursor</cursorShape>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton 
{
    text-align: left;
    color: #ffffff;
    background-color:#2F3C71;
    border-width: 1px;
    border-color: #2F3C71;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
    min-width: 40px;
}

QPushButton:hover
{
    background-color:#4154A0;
}

QPushButton:active
{
    background-color:#4154A0;
}
QPushButton:pressed
{
    background-color: #384889;
 	border-width: 3px;
    border-color: #5C70BC;
    border-style: solid;
    border-radius: 6;

}</string>
     </property>
     <property name="text">
      <string>Personnel Location</string>
     </property>
     <property name="icon">
      <iconset resource="../IconResource.qrc">
       <normaloff>:/images/locate.png</normaloff>:/images/locate.png</iconset>
     </property>
     <property name="iconSize">
      <size>
       <width>25</width>
       <height>25</height>
      </size>
     </property>
     <property name="flat">
      <bool>false</bool>
     </property>
    </widget>
    <widget class="QPushButton" name="navViewMangement">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>47</y>
       <width>290</width>
       <height>44</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Segoe UI</family>
       <pointsize>11</pointsize>
      </font>
     </property>
     <property name="cursor">
      <cursorShape>PointingHandCursor</cursorShape>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton 
{
    text-align: left;
    color: #ffffff;
    background-color:#2F3C71;
    border-width: 1px;
    border-color: #2F3C71;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
    min-width: 40px;
}

QPushButton:hover
{
    background-color:#4154A0;
}
QPushButton:pressed
{
    background-color: #384889;
 	border-width: 3px;
    border-color: #5C70BC;
    border-style: solid;
    border-radius: 6;

}</string>
     </property>
     <property name="text">
      <string>Personnel Management System</string>
     </property>
     <property name="icon">
      <iconset resource="../IconResource.qrc">
       <normaloff>:/images/personnel.png</normaloff>:/images/personnel.png</iconset>
     </property>
     <property name="iconSize">
      <size>
       <width>32</width>
       <height>32</height>
      </size>
     </property>
     <property name="flat">
      <bool>false</bool>
     </property>
    </widget>
    <widget class="QPushButton" name="navViewPPE">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>719</y>
       <width>290</width>
       <height>44</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Segoe UI</family>
       <pointsize>11</pointsize>
      </font>
     </property>
     <property name="cursor">
      <cursorShape>PointingHandCursor</cursorShape>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton 
{
    text-align: left;
    color: #ffffff;
    background-color:#2F3C71;
    border-width: 1px;
    border-color: #2F3C71;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
    min-width: 40px;
}

QPushButton:hover
{
    background-color:#4154A0;
}
QPushButton:pressed
{
    background-color: #384889;
 	border-width: 3px;
    border-color: #5C70BC;
    border-style: solid;
    border-radius: 6;

}</string>
     </property>
     <property name="text">
      <string>Small Arm and PPE Book</string>
     </property>
     <property name="icon">
      <iconset resource="../IconResource.qrc">
       <normaloff>:/images/armPPE.png</normaloff>:/images/armPPE.png</iconset>
     </property>
     <property name="iconSize">
      <size>
       <width>25</width>
       <height>25</height>
      </size>
     </property>
     <property name="flat">
      <bool>false</bool>
     </property>
    </widget>
    <widget class="QPushButton" name="navViewOOD">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>631</y>
       <width>290</width>
       <height>44</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Segoe UI</family>
       <pointsize>11</pointsize>
      </font>
     </property>
     <property name="cursor">
      <cursorShape>PointingHandCursor</cursorShape>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton 
{
    text-align: left;
    color: #ffffff;
    background-color:#2F3C71;
    border-width: 1px;
    border-color: #2F3C71;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
    min-width: 40px;
}

QPushButton:hover
{
    background-color:#4154A0;
}
QPushButton:pressed
{
    background-color: #384889;
 	border-width: 3px;
    border-color: #5C70BC;
    border-style: solid;
    border-radius: 6;

}</string>
     </property>
     <property name="text">
      <string>OOD Observation Book</string>
     </property>
     <property name="icon">
      <iconset resource="../IconResource.qrc">
       <normaloff>:/images/oodObserve.png</normaloff>:/images/oodObserve.png</iconset>
     </property>
     <property name="iconSize">
      <size>
       <width>25</width>
       <height>25</height>
      </size>
     </property>
     <property name="flat">
      <bool>false</bool>
     </property>
    </widget>
    <widget class="QPushButton" name="navViewCMS">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>135</y>
       <width>290</width>
       <height>44</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Segoe UI</family>
       <pointsize>11</pointsize>
      </font>
     </property>
     <property name="cursor">
      <cursorShape>PointingHandCursor</cursorShape>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton 
{
    text-align: left;
    color: #ffffff;
    background-color:#2F3C71;
    border-width: 1px;
    border-color: #2F3C71;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
    min-width: 40px;
}

QPushButton:hover
{
    background-color:#4154A0;
}
QPushButton:pressed
{
    background-color: #384889;
 	border-width: 3px;
    border-color: #5C70BC;
    border-style: solid;
    border-radius: 6;

}</string>
     </property>
     <property name="text">
      <string>SRE Call Management System</string>
     </property>
     <property name="icon">
      <iconset resource="../IconResource.qrc">
       <normaloff>:/images/sreCall.png</normaloff>:/images/sreCall.png</iconset>
     </property>
     <property name="iconSize">
      <size>
       <width>25</width>
       <height>25</height>
      </size>
     </property>
     <property name="flat">
      <bool>false</bool>
     </property>
    </widget>
    <widget class="QPushButton" name="pushButton">
     <property name="enabled">
      <bool>true</bool>
     </property>
     <property name="geometry">
      <rect>
       <x>1080</x>
       <y>5</y>
       <width>260</width>
       <height>35</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Segoe UI</family>
       <pointsize>11</pointsize>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true"> text-align: right;
    color: #ffffff;
    background-color:#222222;</string>
     </property>
     <property name="text">
      <string>Personnel Location</string>
     </property>
     <property name="icon">
      <iconset resource="../IconResource.qrc">
       <normaloff>:/images/personnel.png</normaloff>:/images/personnel.png</iconset>
     </property>
     <property name="iconSize">
      <size>
       <width>32</width>
       <height>32</height>
      </size>
     </property>
    </widget>
    <widget class="QPushButton" name="pushButton_2">
     <property name="enabled">
      <bool>true</bool>
     </property>
     <property name="geometry">
      <rect>
       <x>316</x>
       <y>680</y>
       <width>100</width>
       <height>80</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true"> border:1px solid #fff;
    border-radius:4px;
    outline:none;</string>
     </property>
     <property name="text">
      <string/>
     </property>
     <property name="icon">
      <iconset resource="../IconResource.qrc">
       <normaloff>:/images/logoMTIP.png</normaloff>:/images/logoMTIP.png</iconset>
     </property>
     <property name="iconSize">
      <size>
       <width>200</width>
       <height>200</height>
      </size>
     </property>
    </widget>
    <widget class="QPushButton" name="navViewPersonnel">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>279</y>
       <width>290</width>
       <height>44</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Segoe UI</family>
       <pointsize>11</pointsize>
      </font>
     </property>
     <property name="cursor">
      <cursorShape>PointingHandCursor</cursorShape>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton 
{
    text-align: left;
    color: #ffffff;
    background-color:#2F3C71;
    border-width: 1px;
    border-color: #2F3C71;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
    min-width: 40px;
}

QPushButton:hover
{
    background-color:#4154A0;
}

QPushButton:pressed
{
    background-color: #384889;
 	border-width: 3px;
    border-color: #5C70BC;
    border-style: solid;
    border-radius: 6;

}</string>
     </property>
     <property name="text">
      <string>Personnel Data Book</string>
     </property>
     <property name="icon">
      <iconset resource="../IconResource.qrc">
       <normaloff>:/images/personnelData.png</normaloff>:/images/personnelData.png</iconset>
     </property>
     <property name="iconSize">
      <size>
       <width>25</width>
       <height>25</height>
      </size>
     </property>
     <property name="flat">
      <bool>false</bool>
     </property>
    </widget>
    <widget class="QPushButton" name="navViewState">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>179</y>
       <width>290</width>
       <height>44</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Segoe UI</family>
       <pointsize>11</pointsize>
      </font>
     </property>
     <property name="cursor">
      <cursorShape>PointingHandCursor</cursorShape>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton 
{
    text-align: left;
    color: #ffffff;
    background-color:#2F3C71;
    border-width: 1px;
    border-color: #2F3C71;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
    min-width: 40px;
}

QPushButton:hover
{
    background-color:#4154A0;
}
QPushButton:pressed
{
    background-color: #384889;
 	border-width: 3px;
    border-color: #5C70BC;
    border-style: solid;
    border-radius: 6;

}</string>
     </property>
     <property name="text">
      <string>Personnel State Management System</string>
     </property>
     <property name="icon">
      <iconset resource="../IconResource.qrc">
       <normaloff>:/images/armoryState.png</normaloff>:/images/armoryState.png</iconset>
     </property>
     <property name="iconSize">
      <size>
       <width>25</width>
       <height>25</height>
      </size>
     </property>
     <property name="flat">
      <bool>false</bool>
     </property>
    </widget>
    <widget class="QScrollArea" name="scrollArea">
     <property name="geometry">
      <rect>
       <x>325</x>
       <y>60</y>
       <width>1025</width>
       <height>551</height>
      </rect>
     </property>
     <property name="widgetResizable">
      <bool>true</bool>
     </property>
     <widget class="QWidget" name="scrollAreaWidgetContents_4">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>0</y>
        <width>1023</width>
        <height>549</height>
       </rect>
      </property>
      <widget class="QPushButton" name="btnshipImage">
       <property name="geometry">
        <rect>
         <x>-10</x>
         <y>-10</y>
         <width>1040</width>
         <height>569</height>
        </rect>
       </property>
       <property name="layoutDirection">
        <enum>Qt::RightToLeft</enum>
       </property>
       <property name="styleSheet">
        <string notr="true">border:1px solid #fff;
outline:none;
background-color:#AADAFF;
color:#AADAFF;</string>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset resource="../IconResource.qrc">
         <normaloff>:/images/shipDefault.png</normaloff>:/images/shipDefault.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>1800</width>
         <height>520</height>
        </size>
       </property>
      </widget>
      <widget class="QPushButton" name="btnZoomIn">
       <property name="geometry">
        <rect>
         <x>974</x>
         <y>6</y>
         <width>44</width>
         <height>44</height>
        </rect>
       </property>
       <property name="font">
        <font>
         <family>Segoe UI</family>
         <pointsize>11</pointsize>
        </font>
       </property>
       <property name="cursor">
        <cursorShape>PointingHandCursor</cursorShape>
       </property>
       <property name="styleSheet">
        <string notr="true">QPushButton
{
    color: #000000;
    background-color:#ffffff;
    border-width: 1px;
    border-color: #A5A5A5;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
}

QPushButton:hover
{
    background-color:#E5E5E5
}
QPushButton:pressed
{
    background-color: #D1D1D1;
 	border-width: 3px;
    border-color: #E5E5E5;
    border-style: solid;
    border-radius: 6;

}</string>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset resource="../IconResource.qrc">
         <normaloff>:/images/zoomIn.png</normaloff>:/images/zoomIn.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>25</width>
         <height>25</height>
        </size>
       </property>
      </widget>
      <widget class="QPushButton" name="btnZoomOut">
       <property name="geometry">
        <rect>
         <x>974</x>
         <y>56</y>
         <width>44</width>
         <height>44</height>
        </rect>
       </property>
       <property name="font">
        <font>
         <family>Segoe UI</family>
         <pointsize>11</pointsize>
        </font>
       </property>
       <property name="cursor">
        <cursorShape>PointingHandCursor</cursorShape>
       </property>
       <property name="styleSheet">
        <string notr="true">QPushButton
{
    color: #000000;
    background-color:#ffffff;
    border-width: 1px;
    border-color: #A5A5A5;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
}

QPushButton:hover
{
    background-color:#E5E5E5
}
QPushButton:pressed
{
    background-color: #D1D1D1;
 	border-width: 3px;
    border-color: #E5E5E5;
    border-style: solid;
    border-radius: 6;

}</string>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset resource="../IconResource.qrc">
         <normaloff>:/images/zoomOut.png</normaloff>:/images/zoomOut.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>25</width>
         <height>25</height>
        </size>
       </property>
      </widget>
      <widget class="QPushButton" name="btnMoveRight">
       <property name="geometry">
        <rect>
         <x>974</x>
         <y>500</y>
         <width>44</width>
         <height>44</height>
        </rect>
       </property>
       <property name="font">
        <font>
         <family>Segoe UI</family>
         <pointsize>11</pointsize>
        </font>
       </property>
       <property name="cursor">
        <cursorShape>PointingHandCursor</cursorShape>
       </property>
       <property name="styleSheet">
        <string notr="true">QPushButton
{
    color: #000000;
    background-color:#ffffff;
    border-width: 1px;
    border-color: #A5A5A5;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
}

QPushButton:hover
{
    background-color:#E5E5E5
}
QPushButton:pressed
{
    background-color: #D1D1D1;
 	border-width: 3px;
    border-color: #E5E5E5;
    border-style: solid;
    border-radius: 6;

}</string>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset resource="../IconResource.qrc">
         <normaloff>:/images/moveRight.png</normaloff>:/images/moveRight.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>25</width>
         <height>25</height>
        </size>
       </property>
      </widget>
      <widget class="QPushButton" name="btnMoveLeft">
       <property name="geometry">
        <rect>
         <x>924</x>
         <y>500</y>
         <width>44</width>
         <height>44</height>
        </rect>
       </property>
       <property name="font">
        <font>
         <family>Segoe UI</family>
         <pointsize>11</pointsize>
        </font>
       </property>
       <property name="cursor">
        <cursorShape>PointingHandCursor</cursorShape>
       </property>
       <property name="styleSheet">
        <string notr="true">QPushButton
{
    color: #000000;
    background-color:#ffffff;
    border-width: 1px;
    border-color: #A5A5A5;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
}

QPushButton:hover
{
    background-color:#E5E5E5
}
QPushButton:pressed
{
    background-color: #D1D1D1;
 	border-width: 3px;
    border-color: #E5E5E5;
    border-style: solid;
    border-radius: 6;

}</string>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset resource="../IconResource.qrc">
         <normaloff>:/images/moveLeft.png</normaloff>:/images/moveLeft.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>25</width>
         <height>25</height>
        </size>
       </property>
      </widget>
      <widget class="QPushButton" name="btnMarker2Room2">
       <property name="geometry">
        <rect>
         <x>637</x>
         <y>162</y>
         <width>51</width>
         <height>101</height>
        </rect>
       </property>
       <property name="font">
        <font>
         <family>Segoe UI</family>
         <pointsize>11</pointsize>
        </font>
       </property>
       <property name="cursor">
        <cursorShape>PointingHandCursor</cursorShape>
       </property>
       <property name="styleSheet">
        <string notr="true">QPushButton
{
   
    background-color:transparent;

}</string>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset resource="../IconResource.qrc">
         <normaloff>:/images/markerRoom3.png</normaloff>:/images/markerRoom3.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>75</width>
         <height>75</height>
        </size>
       </property>
      </widget>
      <widget class="QPushButton" name="btnMarker1Room2">
       <property name="geometry">
        <rect>
         <x>562</x>
         <y>162</y>
         <width>51</width>
         <height>101</height>
        </rect>
       </property>
       <property name="font">
        <font>
         <family>Segoe UI</family>
         <pointsize>11</pointsize>
        </font>
       </property>
       <property name="cursor">
        <cursorShape>PointingHandCursor</cursorShape>
       </property>
       <property name="styleSheet">
        <string notr="true">QPushButton
{
   
    background-color:transparent;

}</string>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset resource="../IconResource.qrc">
         <normaloff>:/images/markerRoom3.png</normaloff>:/images/markerRoom3.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>75</width>
         <height>75</height>
        </size>
       </property>
      </widget>
      <widget class="QPushButton" name="btnMarker3Room1">
       <property name="geometry">
        <rect>
         <x>466</x>
         <y>163</y>
         <width>51</width>
         <height>101</height>
        </rect>
       </property>
       <property name="font">
        <font>
         <family>Segoe UI</family>
         <pointsize>11</pointsize>
        </font>
       </property>
       <property name="cursor">
        <cursorShape>PointingHandCursor</cursorShape>
       </property>
       <property name="styleSheet">
        <string notr="true">QPushButton
{
   
    background-color:transparent;

}</string>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset resource="../IconResource.qrc">
         <normaloff>:/images/markerRoom2.png</normaloff>:/images/markerRoom2.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>75</width>
         <height>75</height>
        </size>
       </property>
      </widget>
      <widget class="QPushButton" name="btnMarker2Room1">
       <property name="geometry">
        <rect>
         <x>403</x>
         <y>240</y>
         <width>101</width>
         <height>51</height>
        </rect>
       </property>
       <property name="font">
        <font>
         <family>Segoe UI</family>
         <pointsize>11</pointsize>
        </font>
       </property>
       <property name="cursor">
        <cursorShape>PointingHandCursor</cursorShape>
       </property>
       <property name="styleSheet">
        <string notr="true">QPushButton
{
   
    background-color:transparent;

}</string>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset resource="../IconResource.qrc">
         <normaloff>:/images/markerRoomLeft2.png</normaloff>:/images/markerRoomLeft2.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>75</width>
         <height>75</height>
        </size>
       </property>
      </widget>
      <widget class="QPushButton" name="btnMarker1Room3">
       <property name="geometry">
        <rect>
         <x>542</x>
         <y>298</y>
         <width>51</width>
         <height>101</height>
        </rect>
       </property>
       <property name="font">
        <font>
         <family>Segoe UI</family>
         <pointsize>11</pointsize>
        </font>
       </property>
       <property name="cursor">
        <cursorShape>PointingHandCursor</cursorShape>
       </property>
       <property name="styleSheet">
        <string notr="true">QPushButton
{
   
    background-color:transparent;

}</string>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset resource="../IconResource.qrc">
         <normaloff>:/images/markerRoom1.png</normaloff>:/images/markerRoom1.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>75</width>
         <height>75</height>
        </size>
       </property>
      </widget>
      <widget class="QPushButton" name="btnMarker2Room3">
       <property name="geometry">
        <rect>
         <x>612</x>
         <y>298</y>
         <width>51</width>
         <height>101</height>
        </rect>
       </property>
       <property name="font">
        <font>
         <family>Segoe UI</family>
         <pointsize>11</pointsize>
        </font>
       </property>
       <property name="cursor">
        <cursorShape>PointingHandCursor</cursorShape>
       </property>
       <property name="layoutDirection">
        <enum>Qt::RightToLeft</enum>
       </property>
       <property name="styleSheet">
        <string notr="true">QPushButton
{
   
    background-color:transparent;

}</string>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset resource="../IconResource.qrc">
         <normaloff>:/images/markerRoom1.png</normaloff>:/images/markerRoom1.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>75</width>
         <height>75</height>
        </size>
       </property>
      </widget>
      <widget class="QPushButton" name="btnMarker1Room1">
       <property name="geometry">
        <rect>
         <x>466</x>
         <y>258</y>
         <width>51</width>
         <height>101</height>
        </rect>
       </property>
       <property name="font">
        <font>
         <family>Segoe UI</family>
         <pointsize>11</pointsize>
        </font>
       </property>
       <property name="cursor">
        <cursorShape>PointingHandCursor</cursorShape>
       </property>
       <property name="styleSheet">
        <string notr="true">QPushButton
{
   
    background-color:transparent;

}</string>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset resource="../IconResource.qrc">
         <normaloff>:/images/markerRoomDown2.png</normaloff>:/images/markerRoomDown2.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>75</width>
         <height>75</height>
        </size>
       </property>
      </widget>
      <widget class="QPushButton" name="btnMarker3Room3">
       <property name="geometry">
        <rect>
         <x>649</x>
         <y>286</y>
         <width>101</width>
         <height>51</height>
        </rect>
       </property>
       <property name="font">
        <font>
         <family>Segoe UI</family>
         <pointsize>11</pointsize>
        </font>
       </property>
       <property name="cursor">
        <cursorShape>PointingHandCursor</cursorShape>
       </property>
       <property name="styleSheet">
        <string notr="true">QPushButton
{
   
    background-color:transparent;

}</string>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset resource="../IconResource.qrc">
         <normaloff>:/images/markerRoomRight1.png</normaloff>:/images/markerRoomRight1.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>75</width>
         <height>75</height>
        </size>
       </property>
      </widget>
      <widget class="QPushButton" name="btnMarker3Room2">
       <property name="geometry">
        <rect>
         <x>649</x>
         <y>240</y>
         <width>101</width>
         <height>51</height>
        </rect>
       </property>
       <property name="font">
        <font>
         <family>Segoe UI</family>
         <pointsize>11</pointsize>
        </font>
       </property>
       <property name="cursor">
        <cursorShape>PointingHandCursor</cursorShape>
       </property>
       <property name="styleSheet">
        <string notr="true">QPushButton
{
   
    background-color:transparent;

}</string>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset resource="../IconResource.qrc">
         <normaloff>:/images/markerRoomRight3.png</normaloff>:/images/markerRoomRight3.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>75</width>
         <height>75</height>
        </size>
       </property>
      </widget>
      <widget class="QPushButton" name="btnMobError">
       <property name="enabled">
        <bool>true</bool>
       </property>
       <property name="geometry">
        <rect>
         <x>6</x>
         <y>482</y>
         <width>211</width>
         <height>61</height>
        </rect>
       </property>
       <property name="font">
        <font>
         <family>Segoe UI</family>
         <pointsize>11</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">border:1px solid  #FF5555;
background-color: #FF5555;
outline:none;
color: #FFFFFF;</string>
       </property>
       <property name="text">
        <string>Alert! Man Overboard!</string>
       </property>
       <property name="icon">
        <iconset resource="../IconResource.qrc">
         <normaloff>:/images/notification.png</normaloff>:/images/notification.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>32</width>
         <height>32</height>
        </size>
       </property>
      </widget>
      <zorder>btnshipImage</zorder>
      <zorder>btnMarker2Room2</zorder>
      <zorder>btnMarker1Room2</zorder>
      <zorder>btnMarker3Room1</zorder>
      <zorder>btnMarker2Room1</zorder>
      <zorder>btnMarker1Room3</zorder>
      <zorder>btnMarker2Room3</zorder>
      <zorder>btnMarker1Room1</zorder>
      <zorder>btnMarker3Room3</zorder>
      <zorder>btnMarker3Room2</zorder>
      <zorder>btnMoveLeft</zorder>
      <zorder>btnMoveRight</zorder>
      <zorder>btnZoomIn</zorder>
      <zorder>btnZoomOut</zorder>
      <zorder>btnMobError</zorder>
     </widget>
    </widget>
    <widget class="QPushButton" name="navViewState_2">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>223</y>
       <width>290</width>
       <height>44</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Segoe UI</family>
       <pointsize>11</pointsize>
      </font>
     </property>
     <property name="cursor">
      <cursorShape>PointingHandCursor</cursorShape>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton 
{
    text-align: left;
    color: #ffffff;
    background-color:#2F3C71;
    border-width: 1px;
    border-color: #2F3C71;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 11pt;
    padding-left: 5px;
    padding-right: 5px;
    min-width: 40px;
}

QPushButton:hover
{
    background-color:#4154A0;
}
QPushButton:pressed
{
    background-color: #384889;
 	border-width: 3px;
    border-color: #5C70BC;
    border-style: solid;
    border-radius: 6;

}</string>
     </property>
     <property name="text">
      <string>Armory State Management System</string>
     </property>
     <property name="icon">
      <iconset resource="../IconResource.qrc">
       <normaloff>:/images/armoryState.png</normaloff>:/images/armoryState.png</iconset>
     </property>
     <property name="iconSize">
      <size>
       <width>25</width>
       <height>25</height>
      </size>
     </property>
     <property name="flat">
      <bool>false</bool>
     </property>
    </widget>
    <zorder>label_2</zorder>
    <zorder>label</zorder>
    <zorder>navViewPunishment</zorder>
    <zorder>navViewImpKey</zorder>
    <zorder>navViewGenKey</zorder>
    <zorder>navViewVisitor</zorder>
    <zorder>navViewTransport</zorder>
    <zorder>navViewGangway</zorder>
    <zorder>navViewDuty</zorder>
    <zorder>navViewNight</zorder>
    <zorder>label_4</zorder>
    <zorder>navViewMOB</zorder>
    <zorder>navViewLocation</zorder>
    <zorder>navViewMangement</zorder>
    <zorder>navViewPPE</zorder>
    <zorder>navViewOOD</zorder>
    <zorder>navViewCMS</zorder>
    <zorder>pushButton</zorder>
    <zorder>pushButton_2</zorder>
    <zorder>navViewPersonnel</zorder>
    <zorder>navViewState</zorder>
    <zorder>scrollArea</zorder>
    <zorder>navViewState_2</zorder>
   </widget>
  </widget>
 </widget>
 <resources>
  <include location="../IconResource.qrc"/>
 </resources>
 <connections/>
</ui>
