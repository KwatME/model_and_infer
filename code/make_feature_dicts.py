import gzip
import pickle

import ccal


def make_feature_dicts():

    pickle_gz_file_path = '../data/ccle.pickle.gz'

    feature_groups = (
        'Mutation',
        'Mutational Signature',
        'CNV',
        'Methylation',
        'RNA',
        'Gene Set',
        'Protein',
        'Metabolite',
        'RNAi',
        'CRISPR',
        'NP24',
        'CTRP',
        # 'Information',
    )

    #     pickle_gz_file_path = '../data/tcga.pickle.gz'

    #     feature_groups = (
    #         'Mutation',
    #         'Mutational Signature',
    #         'CNV',
    #         'Methylation',
    #         'RNA',
    #         'miRNA',
    #         'Gene Set',
    #         'Protein',
    #         'Immune Signature',
    #         'Continuous Information',
    #         'Binary Information',
    #     )

    feature_group_features = {}

    with gzip.open(pickle_gz_file_path) as pickle_gz_file:

        feature_dicts = pickle.load(pickle_gz_file)

    feature_dicts = {
        feature_group: feature_dicts[feature_group]
        for feature_group in feature_groups
    }

    for feature_group, features in feature_group_features.items():

        for feature in features:

            feature_dicts['{} {}'.format(
                feature_group,
                feature,
            )] = {
                'df':
                ccal.make_membership_df_from_categorical_series(
                    feature_dicts[feature_group]['df'].loc[feature]).astype(
                        int),
                'data_type':
                'binary',
                'emphasis':
                'high',
            }

    return feature_dicts
