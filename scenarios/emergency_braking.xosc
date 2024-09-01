<?xml version="1.0" encoding="UTF-8"?>
<OpenScenario xmlns="http://www.asam.net/xml/schemas/openSCENARIO/1.2">
    <FileHeader
        vendor="YourCompany"
        name="Emergency Braking Scenario"
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
                <Performance maxSpeed="50" maxAcceleration="3.0" maxDeceleration="8.0"/>
                <BoundingBox dimensions="4.5,1.8,1.5"/>
                <Axles/>
            </Vehicle>
        </Entity>
        <!-- Leading Vehicle -->
        <Entity name="LeadingVehicle">
            <Vehicle>
                <Performance maxSpeed="50" maxAcceleration="2.5" maxDeceleration="5.0"/>
                <BoundingBox dimensions="4.5,1.8,1.5"/>
                <Axles/>
            </Vehicle>
        </Entity>
    </Entities>
    <Storyboard>
        <Init>
            <!-- Position Autonomous Vehicle behind Leading Vehicle -->
            <Position>
                <EntityRef entity="AutonomousVehicle"/>
                <WorldPosition x="0" y="0" z="0" h="0" p="0" r="0"/>
            </Position>
            <Position>
                <EntityRef entity="LeadingVehicle"/>
                <WorldPosition x="30" y="0" z="0" h="0" p="0" r="0"/>
            </Position>
        </Init>
        <Stories>
            <Story name="EmergencyBraking">
                <Acts>
                    <Act name="NormalDriving">
                        <Maneuver name="MaintainSpeed">
                            <Event name="MaintainSpeedEvent" priority="overwrite">
                                <Action name="MaintainSpeedAction">
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
                    <Act name="BrakeEmergency">
                        <Maneuver name="PerformEmergencyBrake">
                            <Event name="EmergencyBrakeEvent" priority="overwrite">
                                <Action name="EmergencyBrakeAction">
                                    <PrivateAction>
                                        <LongitudinalAction>
                                            <SpeedAction>
                                                <SpeedActionDynamics dynamicsShape="step" value="0"/>
                                                <SpeedTarget>
                                                    <AbsoluteSpeed value="0"/>
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
