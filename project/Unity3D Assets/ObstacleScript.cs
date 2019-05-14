using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using MLAgents;

public class ObstacleScript : MonoBehaviour
{
    private void OnTriggerEnter(Collider other)
    {
        // Get a link to the PilotAgent script
        Transform ship = other.transform.parent;
        Agent pilot = ship.GetComponent<Agent>();

        if (pilot != null)
        {
            // Penalize the pilot for running into a wall
            pilot.AddReward(-1);
            pilot.Done();
        }
    }
}
