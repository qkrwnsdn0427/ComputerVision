import os
import zipfile

_A2_FILES = ["pytorch_tutorial.py", "pytorch_tutorial.ipynb", "knn.py", "knn.ipynb"]

_A3_FILES = [
    "linear_classifier.py",
    "linear_classifier.ipynb",
    "two_layer_net.py",
    "two_layer_net.ipynb",
    "svm_best_model.pt",
    "softmax_best_model.pt",
    "nn_best_model.pt",
]

_A4_FILES = [
    "fully_connected_networks.py",
    "fully_connected_networks.ipynb",
    "convolutional_networks.py",
    "convolutional_networks.ipynb",
    "best_overfit_five_layer_net.pth",
    "best_two_layer_net.pth",
    "one_minute_deepconvnet.pth",
    "overfit_deepconvnet.pth",
]

_A5_FILES = [
    "common.py",
    "one_stage_detector.py",
    "two_stage_detector.py",
    "one_stage_detector.ipynb",
    "two_stage_detector.ipynb",
    "fcos_detector.pt",
    "rcnn_detector.pt",
]

_A6_FILES = [
    "transformers.py",
    "Transformers.ipynb",
    "rnn_lstm_captioning.py",
    "rnn_lstm_captioning.ipynb",
    # result files
    "transformer.pt",
    "rnn_lstm_attention_submission.pt",
]

_A7_FILES = [
    "vae.py",
    "variational_autoencoders.ipynb",
    "gan.py",
    "generative_adversarial_networks.ipynb",
    "network_visualization.py",
    "network_visualization.ipynb",
    "style_transfer.py",
    "style_transfer.ipynb",
    # result_files
    "vae_generation.jpg",
    "conditional_vae_generation.jpg",
    "fc_gan_results.jpg",
    "ls_gan_results.jpg",
    "dc_gan_results.jpg",
    "saliency_maps_results.jpg",
    "adversarial_attacks_results.jpg",
    "class_viz_result.jpg",
    "style_transfer_result.jpg",
    "feature_inversion_result.jpg",
    "spatial_style_transfer_result.jpg",
]


def make_a2_submission(assignment_path, uniquename=None, hyid=None):
    _make_submission(assignment_path, _A2_FILES, "A2", uniquename, hyid)


def make_a3_submission(assignment_path, uniquename=None, hyid=None):
    _make_submission(assignment_path, _A3_FILES, "A3", uniquename, hyid)


def make_a4_submission(assignment_path, uniquename=None, hyid=None):
    _make_submission(assignment_path, _A4_FILES, "A4", uniquename, hyid)


def make_a5_submission(assignment_path, uniquename=None, hyid=None):
    _make_submission(assignment_path, _A5_FILES, "A5", uniquename, hyid)


def make_a6_submission(assignment_path, uniquename=None, hyid=None):
    _make_submission(assignment_path, _A6_FILES, "A6", uniquename, hyid)


def make_a7_submission(assignment_path, uniquename=None, hyid=None):
    _make_submission(assignment_path, _A7_FILES, "A7", uniquename, hyid)


def _make_submission(
    assignment_path, file_list, assignment_no, uniquename=None, hyid=None
):
    if uniquename is None or hyid is None:
        uniquename, hyid = _get_user_info()
    zip_path = f"{uniquename}_{hyid}_{assignment_no}.zip"
    zip_path = os.path.join(assignment_path, zip_path)
    print("Writing zip file to: ", zip_path)
    with zipfile.ZipFile(zip_path, "w") as zf:
        for filename in file_list:
            if filename.startswith("ite4052/"):
                filename_out = filename.split("/")[-1]
            else:
                filename_out = filename
            in_path = os.path.join(assignment_path, filename)
            if not os.path.isfile(in_path):
                raise ValueError('Could not find file "%s"' % filename)
            zf.write(in_path, filename_out)


def _get_user_info():
    uniquename = None
    hyid = None
    if uniquename is None:
        uniquename = input("Enter your uniquename (e.g. sukminyun): ")
    if hyid is None:
        hyid = input("Enter your hyid (e.g. 12345678): ")
    return uniquename, hyid
