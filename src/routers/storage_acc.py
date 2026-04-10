from flask import Blueprint, jsonify
from cust_func.var_storage import save_kernel_state, load_kernel_state

storage_acc_bp = Blueprint('/kernels', __name__)

@storage_acc_bp.route('/get_kernel_state', methods=['GET'])
def get_storage_acc():
    variables = load_kernel_state()
    return jsonify(variables)