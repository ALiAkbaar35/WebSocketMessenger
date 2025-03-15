from flask import Blueprint, request, jsonify
jobsapi = Blueprint('jobs', __name__, url_prefix='/jobs')
from app.jobs.controller import add_JOB, get_jobs, get_job_by_id, get_del_job_by_id, update_job_id, filter_title, add_multiple_jobs

@jobsapi.route("/", methods=["POST"])
def handle_add_jobs():
    try:
        data = request.json
        response = add_JOB(data)
        return response
    except Exception as e:
        return jsonify({"error": f"Failed to add job: {str(e)}"})

@jobsapi.route("/", methods=['GET'])
def handle_get_jobs():
    try:
        response = get_jobs()
        return response
    except Exception as e:
        return jsonify({"error": f"Failed to retrieve jobs: {str(e)}"})

@jobsapi.route('/<int:job_id>', methods=['GET'])
def get_job(job_id):
    try:
        response = get_job_by_id(job_id)
        return response
    except Exception as e:
        return jsonify({"error": f"Failed to retrieve job: {str(e)}"})

@jobsapi.route('/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    try:
        response = get_del_job_by_id(job_id)
        return response
    except Exception as e:
        return jsonify({"error": f"Failed to delete job: {str(e)}"})

@jobsapi.route('/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    try:
        data = update_job_id(job_id, request.json)
        return data
    except Exception as e:
        return jsonify({"error": f"Failed to update job: {str(e)}"})
    
@jobsapi.route('/title/<string:title>', methods=['GET'])
def filter_by_title(title):
    try:
        data = filter_title(title)
        return data
    except Exception as e:
        return jsonify({"error": f"Failed to filter jobs by title: {str(e)}"})
    
@jobsapi.route('/bulk', methods=['POST'])
def handle_add_multiple_jobs():
    try:
        data = request.json
        # Ensure the incoming data is a list of job dictionaries
        if not isinstance(data, list):
            return jsonify({"error": "Data must be a list of job objects", "status": 400}), 400

        response = add_multiple_jobs(data)
        return response
    except Exception as e:
        return jsonify({"error": f"Failed to add multiple jobs: {str(e)}", "status": 500}), 500