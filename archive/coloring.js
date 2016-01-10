/**
 * getColor function to return color based on the speed of traffic
 * Ani Kunaparaju - Rice AI Traffic
 * November 7 2015
 */

function getColor(freeflow_speed, current_speed)
{
    var orange = "#F57D02";
    var green = "#84CA50";
    var red = "#E60000";

    if (current_speed <= 0.5*freeflow_speed)
    {
        return red;
    }

    else if (current_speed <= location[speed]*0.8 && current_speed > location[speed]*0.5)
    {
        return orange;
    }

    return green;
}