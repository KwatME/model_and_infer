from pandas import read_csv


def read_ws_hs(mf_directory_path, model_mode, model_data_dicts):

    n_data_dicts = len(model_data_dicts)

    if model_mode == "range":

        n_w = 1

        n_h = n_data_dicts

    elif model_mode == "deep":

        n_w = n_data_dicts

        n_h = 1

    ws = []

    for i in range(n_w):

        w = read_csv("{}/w{}.tsv".format(mf_directory_path, i), sep="\t", index_col=0)

        w.columns.name = "Factor"

        ws.append(w)

    hs = []

    for i in range(n_h):

        h = read_csv("{}/h{}.tsv".format(mf_directory_path, i), sep="\t", index_col=0)

        h.columns.name = model_data_dicts[i]["axis1_name"]

        hs.append(h)

    return ws, hs