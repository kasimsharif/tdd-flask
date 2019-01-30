from flask_restful import Resource
from flask import request, abort, jsonify
from app.models import ChoiceList


class ChoiceListAPI(Resource):
    def get(self, id=None):
        if id:
            choice_list = ChoiceList.query.filter_by(id=id).first()
            if not choice_list:
                abort(404)
            response = jsonify({
                "id": choice_list.id,
                "name": choice_list.name,
                "createdOn": choice_list.created_on,
                "updateOn": choice_list.updated_on
            })
            response.status_code = 200
            return response
        choice_lists = ChoiceList.query.all()
        results = []
        for choice_list in choice_lists:
            results.append({
                "id": choice_list.id,
                "name": choice_list.name,
                "createdOn": choice_list.created_on,
                "updateOn": choice_list.updated_on
            })
        response = jsonify(results)
        return response

    def post(self):
        request_data = request.get_json(force=True)
        name = request_data["name"]
        if name:
            choice_list = ChoiceList(name=name)
            choice_list.save()
            response = jsonify({
                "id": choice_list.id,
                "name": choice_list.name,
                "createdOn": choice_list.created_on,
                "updateOn": choice_list.updated_on
            })
            response.status_code = 201
            return response
