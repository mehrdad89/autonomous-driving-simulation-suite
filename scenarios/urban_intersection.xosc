<?xml version="1.0" encoding="UTF-8"?>
<OpenScenario xmlns="http://www.asam.net/xml/schemas/openSCENARIO/1.2">
    <FileHeader
        vendor="YourCompany"
        name="Urban Intersection Scenario"
        version="1.0"
        date="2024-04-27"/>
    <ParameterDeclarations/>
    <Catalogs/>
    <RoadNetwork>
        <LogicFile filepath="road_networks/city_streets.xodr"/>
    </RoadNetwork>
    <Entities>
        <!-- Autonomous Vehicle -->
        <Entity name="AutonomousVehicle">
            <Vehicle>
                <Performance maxSpeed="50" maxAcceleration="3.0" maxDeceleration="6.0"/>
                <BoundingBox dimensions="4.5,1.8,1.5"/>
                <Axles/>
            </Vehicle>
        </Entity>
        <!-- Cross Traffic Vehicle -->
        <Entity name="CrossTrafficVehicle">
            <Vehicle>
                <Performance maxSpeed="40" maxAcceleration="2.5" maxDeceleration="5.5"/>
                <BoundingBox dimensions="4.5,1.8,1.5"/>
                <Axles/>
            </Vehicle>
        </Entity>
    </Entities>
    <Storyboard>
        <Init>
            <!-- Position Autonomous Vehicle at approach -->
            <Position>
                <EntityRef entity="AutonomousVehicle"/>
                <WorldPosition x="0" y="0" z="0" h="0" p="0" r="0"/>
            </Position>
            <!-- Position Cross Traffic Vehicle waiting to cross -->
            <Position>
                <EntityRef entity="CrossTrafficVehicle"/>
                <WorldPosition x="10" y="10" z="0" h="180" p="0" r="0"/>
            </Position>
        </Init>
        <Stories>
            <Story name="IntersectionNavigation">
                <Acts>
                    <Act name="ApproachIntersection">
                        <Maneuver name="DriveForward">
                            <Event name="StartDriving" priority="overwrite">
                                <Action name="DriveForwardAction">
                                    <PrivateAction>
                                        <LongitudinalAction>
                                            <SpeedAction>
                                                <SpeedActionDynamics dynamicsShape="step" value="50"/>
                                                <SpeedTarget>
                                                    <AbsoluteSpeed value="50"/>
                                                </SpeedTarget>
                                            </SpeedAction>
                                        </LongitudinalAction>
                                    </PrivateAction>
                                </Action>
                            </Event>
                        </Maneuver>
                    </Act>
                    <Act name="CrossTrafficMovement">
                        <Maneuver name="CrossTrafficDrive">
                            <Event name="StartCrossing" priority="overwrite">
                                <Action name="CrossTrafficAction">
                                    <PrivateAction>
                                        <LongitudinalAction>
                                            <SpeedAction>
                                                <SpeedActionDynamics dynamicsShape="step" value="40"/>
                                                <SpeedTarget>
                                                    <AbsoluteSpeed value="40"/>
                                                </SpeedTarget>
                                            </SpeedAction>
                                        </LongitudinalAction>
                                    </PrivateAction>
                                </Action>
                            </Event>
                        </Maneuver>
                    </Act>
                </Acts>
            </Story>
        </Stories>
    </Storyboard>
</OpenScenario>
