using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using MLAgents;
using System.Linq;

public class PilotAgentSM04 : Agent {

    [HideInInspector]
    // The target the ship will run towards.
    public Transform target;

    // These items should be set in the inspector
    // These will be the position points from which to apply forces
    [Header("Rockets")]
    public Transform rearRocket;
    public Transform rightForwardRocket;
    public Transform rightRearRocket;
    public Transform leftForwardRocket;
    public Transform leftRearRocket;

    //JointDriveController jdController;
    Rigidbody rb;

    // original position / rotation (for respawn)
    Vector3 originalPosition;
    Quaternion originalRotation;

    // last position / rotation
    Vector3 lastPosition;
    Quaternion lastRotation;

    [HideInInspector]
    int decisionCounter = 0;
    
    void Awake()
    {
        // setup rigidbody which will be used to apply relevant forces
        rb = GetComponent<Rigidbody>();

        // save off initial state info for respawn
        originalPosition = transform.position;
        originalRotation = transform.rotation;

        // 
        lastRotation = transform.rotation;
        lastPosition = transform.position;
    }

    

    /// <summary>
    /// The method the agent uses to collect information about the environment
    /// </summary>
    public override void CollectObservations() {

        // current location
        AddVectorObs(transform.position);
        AddVectorObs(transform.localPosition);

        // current rotation
        AddVectorObs(transform.rotation);
        AddVectorObs(transform.localRotation);

        // previous location / rotation
        AddVectorObs(lastPosition);
        AddVectorObs(lastRotation);

        // update previous location / rotation
        lastPosition = transform.position;
        lastRotation = transform.rotation;

        // distance to nearest wall
        AddVectorObs(DistanceToNearestWall());
    }

    /// <summary>
    /// The agent's action method. Is called at each decision and allows the agent to move
    /// </summary>
    /// <param name="vectorAction"> The actions that were determined by the policy</param>
    /// <param name="textAction"> The text action given by the policy</param>
	public override void AgentAction(float[] vectorAction, string textAction)
    {
        // apply what the model thinks is appropriate force to each of the rocket thrusters
        rb.AddForceAtPosition(transform.forward * vectorAction[0], rearRocket.position);
        rb.AddForceAtPosition(transform.forward * vectorAction[1], rightForwardRocket.position);
        rb.AddForceAtPosition(transform.forward * vectorAction[2], rightRearRocket.position);
        rb.AddForceAtPosition(transform.forward * vectorAction[3], leftForwardRocket.position);
        rb.AddForceAtPosition(transform.forward * vectorAction[4], leftRearRocket.position);
    }

    void FixedUpdate()
    {

        // keep track of steps to next decision
        // ergo request decision every 3-4 steps
        if (decisionCounter == 0)
        {
            decisionCounter = 3;
            RequestDecision();
        }
        else
        {
            decisionCounter--;
        }

        // Reward for moving forwards
        RewardFunctionForMovingForwards();

        // Penalize it for getting too close to a wall
        RewardProximityPenalty();

        // Penalty for time
        //RewardFunctionTimePenalty();
    }

    /// <summary>
    /// Forward Movement Reward
    /// The spaceship gets a reward for moving forward and a penalty for not moving forward.
    /// </summary>
    void RewardFunctionForMovingForwards()
    {
        // check if we've moved forward
        float forwardMovement = transform.position.z - lastPosition.z;
        if (forwardMovement > 0)
        {
            // reward
            AddReward(0.001f);
        } else
        {
            // penalty
            AddReward(-0.001f);
        }
    }
    
    /// <summary>
    /// Obstacle Proximity Penalty
    /// The spaceship gets a reward for being too close too a wall.
    /// </summary>
    void RewardProximityPenalty()
    {
        // find all nearby obstacles
        var obstacles = Physics.OverlapSphere(
            position: transform.position, 
            radius: 8f
        ).Where(x => x.tag == "Obstacle").ToList();

        // we only really care if we're near at least one
        bool inCloseProximity = obstacles.Count > 0;

        // Inform the ship about the number of nearby objects
        // since it's deserves to know what it's being punished for...
        AddVectorObs(inCloseProximity);

        // Penalize ship for being too close to the walls
        if (inCloseProximity) AddReward(-0.001f);
    }

    /// <summary>
    /// Time penalty
    /// The spaceship gets a pentalty each step so that it tries to finish 
    /// as quickly as possible.
    /// </summary>
    void RewardFunctionTimePenalty()
    {
        AddReward(-0.001f);  //-0.001f was chosen for the Puppo experiment
    }

    public override void AgentReset()
    {
        Respawn();
    }

    private void Respawn()
    {
        // reset position / rotation
        transform.position = originalPosition;
        transform.rotation = originalRotation;

        // clean up rigidbody forces
        rb.velocity = Vector3.zero;
        rb.angularVelocity = Vector3.zero;
    }

    private float DistanceToNearestWall()
    {
        RaycastHit hit;
        if(Physics.Raycast(transform.position, transform.forward, out hit, Mathf.Infinity))
        {
            return hit.distance;
        } else
        {
            return Mathf.Infinity;
        }
    }
}