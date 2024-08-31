<?xml version="1.0" encoding="UTF-8"?>
<OpenDRIVE xmlns="http://www.asam.net/xml/schemas/OpenDRIVE/1.4" revMajor="1" revMinor="4">
    <header revMajor="1" revMinor="4" name="Highway" version="1.0" date="2024-04-27"/>
    <road name="MainHighway" length="2000" id="1" junction="-1">
        <link>
            <predecessor id="-1" elementType="road"/>
            <successor id="-1" elementType="road"/>
        </link>
        <type s="0" type="motorway"/>
        <planView>
            <geometry s="0" x="0" y="0" hdg="0" length="2000">
                <line/>
            </geometry>
        </planView>
        <lanes>
            <laneSection s="0">
                <left>
                    <!-- Lane 2 -->
                    <lane id="2" type="driving" level="false">
                        <width sOffset="0" a="3.5" b="0" c="0" d="0"/>
                    </lane>
                    <!-- Lane 3 -->
                    <lane id="3" type="driving" level="false">
                        <width sOffset="0" a="3.5" b="0", c="0" d="0"/>
                    </lane>
                </left>
                <center>
                    <lane id="0" type="none" level="false"/>
                </center>
                <right>
                    <!-- Lane -1 -->
                    <lane id="-1" type="driving" level="false">
                        <width sOffset="0" a="3.5" b="0", c="0" d="0"/>
                    </lane>
                    <!-- Lane -2 -->
                    <lane id="-2" type="driving" level="false">
                        <width sOffset="0" a="3.5" b="0", c="0" d="0"/>
                    </lane>
                </right>
            </laneSection>
        </lanes>
    </road>
    <!-- On-Ramp Road -->
    <road name="OnRamp" length="500" id="2" junction="-1">
        <link>
            <predecessor id="-1" elementType="road"/>
            <successor id="-1" elementType="road"/>
        </link>
        <type s="0" type="ramp"/>
        <planView>
            <geometry s="0" x="2000" y="0" hdg="0" length="500">
                <line/>
            </geometry>
        </planView>
        <lanes>
            <laneSection s="0">
                <left>
                    <lane id="1" type="driving" level="false">
                        <width sOffset="0" a="3.5" b="0", c="0" d="0"/>
                    </lane>
                </left>
                <center>
                    <lane id="0" type="none" level="false"/>
                </center>
                <right>
                    <lane id="-1" type="driving" level="false">
                        <width sOffset="0" a="3.5" b="0", c="0" d="0"/>
                    </lane>
                </right>
            </laneSection>
        </lanes>
    </road>
</OpenDRIVE>
