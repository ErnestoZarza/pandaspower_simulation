from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status, APIView

from .simulation import run_simulation


class ActivePowerView(generics.RetrieveAPIView):
    """
        Endpoint to retrieve the active power of the previously executed simulation.
        GET http://0.0.0.0:8000/pandapower_api/simulation/active/
    """

    def get(self, request, *args, **kwargs):
        response_data = {
            'message': "No previous simulation has been calculated",
            'status': status.HTTP_404_NOT_FOUND
        }

        try:
            active_power = request.session['active_power']
        except KeyError:
            active_power = None

        if active_power is not None:
            response_data = {
                'active_power': active_power,
                'status': "success"
            }

        return Response(response_data)


class ReactivePowerView(generics.RetrieveAPIView):
    """
        Endpoint to retrieve the reactive power of the previously executed simulation.
        GET http://0.0.0.0:8000/pandapower_api/simulation/reactive/
    """

    def get(self, request, *args, **kwargs):
        response_data = {
            'message': "No previous simulation has been calculated",
            'status': status.HTTP_404_NOT_FOUND
        }

        try:
            reactive_power = request.session['reactive_power']
        except KeyError:
            reactive_power = None


        if reactive_power is not None:
            response_data = {
                'reactive_power': reactive_power,
                'status': "success"
            }

        return Response(response_data)


class SimulationView(APIView):

    """
        Endpoint that launches the simulation using the PandaPower Python module
        POST: http://0.0.0.0:8000/pandapower_api/simulation/create/
    """

    def post(self, request, *args, **kwargs):

        current_active_power, current_reactive_power = run_simulation()
        print(current_active_power, current_reactive_power)
        response_data = {
            'active_power': current_active_power,
            'reactive_power': current_reactive_power,
            'status': "success"
        }

        request.session['active_power'] = current_active_power
        request.session['reactive_power'] = current_reactive_power

        return Response(response_data)
