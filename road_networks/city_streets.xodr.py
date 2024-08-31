<?xml version="1.0" encoding="UTF-8"?>
<OpenDRIVE xmlns="http://www.asam.net/xml/schemas/OpenDRIVE/1.4" revMajor="1" revMinor="4">
    <header revMajor="1" revMinor="4" name="City Streets" version="1.0" date="2024-04-27"/>
    <road name="MainStreet" length="500" id="1" junction="-1">
        <link>
            <predecessor id="-1" elementType="road"/>
            <successor id="-1" elementType="road"/>
        </link>
        <type s="0" type="urban"/>
        <planView>
            <geometry s="0" x="0" y="0" hdg="0" length="500">
                <line/>
            </geometry>
        </planView>
        <lanes>
            <laneSection s="0">
                <left>
                    <lane id="2" type="driving" level="false">
                        <width sOffset="0" a="3.5" b="0" c="0" d="0"/>
                    </lane>
                </left>
                <center>
                    <lane id="0" type="none" level="false"/>
                </center>
                <right>
                    <lane id="-1" type="driving" level="false">
                        <width sOffset="0" a="3.5" b="0" c="0" d="0"/>
                    </lane>
                </right>
            </laneSection>
        </lanes>
    </road>
    <road name="CrossStreet" length="500" id="2" junction="-1">
        <link>
            <predecessor id="-1" elementType="road"/>
            <successor id="-1" elementType="road"/>
        </link>
        <type s="0" type="urban"/>
        <planView>
            <geometry s="0" x="250" y="-250" hdg="1.5708" length="500">
                <line/>
            </geometry>
        </planView>
        <lanes>
            <laneSection s="0">
                <left>
                    <lane id="2" type="driving" level="false">
                        <width sOffset="0" a="3.5" b="0" c="0" d="0"/>
                    </lane>
                </left>
                <center>
                    <lane id="0" type="none" level="false"/>
                </center>
                <right>
                    <lane id="-1" type="driving" level="false">
                        <width sOffset="0" a="3.5" b="0" c="0" d="0"/>
                    </lane>
                </right>
            </laneSection>
        </lanes>
    </road>
    <junction id="1">
        <connection fromRoad="1" toRoad="2" contactPoint="end"/>
        <connection fromRoad="2" toRoad="1" contactPoint="start"/>
    </junction>
</OpenDRIVE>
