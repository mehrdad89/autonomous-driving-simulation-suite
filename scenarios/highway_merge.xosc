<?xml version="1.0" encoding="UTF-8"?>
<OpenScenario xmlns="http://www.asam.net/xml/schemas/openSCENARIO/1.2">
    <FileHeader
        vendor="YourCompany"
        name="Highway Merge Scenario"
        version="1.0"
        date="2024-04-27"/>
    <ParameterDeclarations/>
    <Catalogs/>
    <RoadNetwork>
        <LogicFile filepath="road_networks/highway.xodr"/>
    </RoadNetwork>
    <Entities>
        <!-- Merging Autonomous Vehicle -->
        <Entity name="MergingAutonomousVehicle">
            <Vehicle>
                <Performance maxSpeed="30" maxAcceleration="2.5" maxDeceleration="5.0"/>
                <BoundingBox dimensions="4.5,1.8,1.5"/>
                <Axles/>
            </Vehicle>
        </Entity>
        <!-- Highway Vehicle 1 -->
        <Entity name="HighwayVehicle1">
            <Vehicle>
                <Performance maxSpeed="100" maxAcceleration="3.0" maxDeceleration="6.0"/>
                <BoundingBox dimensions="4.5,1.8,1.5"/>
                <Axles/>
            </Vehicle>
        </Entity>
        <!-- Highway Vehicle 2 -->
        <Entity name="HighwayVehicle2">
            <Vehicle>
                <Performance maxSpeed="100" maxAcceleration="3.0" maxDeceleration="6.0"/>
                <BoundingBox dimensions="4.5,1.8,1.5"/>
                <Axles/>
            </Vehicle>
        </Entity>
    </Entities>
    <Storyboard>
        <Init>
            <!-- Position Merging Vehicle at ramp -->
            <Position>
                <EntityRef entity="MergingAutonomousVehicle"/>
                <WorldPosition x="-50" y="0" z="0" h="90" p="0" r="0"/>
            </Position>
            <!-- Position Highway Vehicles on main lane -->
            <Position>
                <EntityRef entity="HighwayVehicle1"/>
                <WorldPosition x="0" y="0" z="0" h="0" p="0" r="0"/>
            </Position>
            <Position>
                <EntityRef entity="HighwayVehicle2"/>
                <WorldPosition x="100" y="0" z="0" h="0" p="0" r="0"/>
            </Position>
        </Init>
        <Stories>
            <Story name="HighwayMerging">
                <Acts>
                    <Act name="MergingAction">
                        <Maneuver name="MergeOntoHighway">
                            <Event name="StartMerging" priority="overwrite">
                                <Action name="MergeAction">
                                    <PrivateAction>
                                        <LongitudinalAction>
                                            <SpeedAction>
                                                <SpeedActionDynamics dynamicsShape="step" value="30"/>
                                                <SpeedTarget>
                                                    <AbsoluteSpeed value="30"/>
                                                </SpeedTarget>
                                            </SpeedAction>
                                        </LongitudinalAction>
                                    </PrivateAction>
                                </Action>
                            </Event>
                        </Maneuver>
                        <Maneuver name="AdjustSpeed">
                            <Event name="AdjustSpeedEvent" priority="overwrite">
                                <Action name="AdjustSpeedAction">
                                    <PrivateAction>
                                        <LongitudinalAction>
                                            <SpeedAction>
                                                <SpeedActionDynamics dynamicsShape="step" value="100"/>
                                                <SpeedTarget>
                                                    <AbsoluteSpeed value="100"/>
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
