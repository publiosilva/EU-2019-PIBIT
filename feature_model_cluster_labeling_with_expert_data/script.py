def get_cluster_score(cluster_path):
    number_of_feature_models = 0
    cluster_score_counter = 0

    with open(cluster_path) as file:
        for line in file:
            columns = line.split(',')

            for i, column in enumerate(columns):
                value = 0

                if i > 0:
                    value = float(column)

                # Number of features
                if i == 1:
                    if value <= 20:
                        cluster_score_counter += 0.3
                    elif value < 40:
                        cluster_score_counter += 0.2
                    elif value >= 40:
                        cluster_score_counter += 0.1
                # Number of mandatory features
                elif i == 2:
                    if value <= 5:
                        cluster_score_counter += 0.3
                    elif value < 17.5:
                        cluster_score_counter += 0.2
                    elif value >= 17.5:
                        cluster_score_counter += 0.1
                # Number of top features
                elif value == 3:
                    if value <= 3:
                        cluster_score_counter += 0.3
                    elif value <= 6:
                        cluster_score_counter += 0.2
                    elif value <= 9:
                        cluster_score_counter += 0.1
                # Number of leaf features
                elif value == 4:
                    if value <= 10:
                        cluster_score_counter += 0.3
                    elif value < 36:
                        cluster_score_counter += 0.2
                    elif value >= 36:
                        cluster_score_counter += 0.1
                # Depth of tree max
                elif value == 5:
                    if value <= 3:
                        cluster_score_counter += 0.3
                    elif value < 5:
                        cluster_score_counter += 0.2
                    elif value >= 5:
                        cluster_score_counter += 0.1
                # Cognitive complexity of a feature model
                elif value == 6:
                    if value <= 3:
                        cluster_score_counter += 0.3
                    elif value < 8:
                        cluster_score_counter += 0.2
                    elif value >= 8:
                        cluster_score_counter += 0.1
                # Feature extendibility
                elif value == 7:
                    if value <= 20:
                        cluster_score_counter += 0.1
                    elif value < 35:
                        cluster_score_counter += 0.2
                    elif value >= 35:
                        cluster_score_counter += 0.3
                # Flexibility of configuration
                elif value == 8:
                    if value <= 0.2:
                        cluster_score_counter += 0.1
                    elif value < 0.4:
                        cluster_score_counter += 0.2
                    elif value >= 0.4:
                        cluster_score_counter += 0.3
                # Single cyclic dependent features
                elif value == 9:
                    if value <= 0.8:
                        cluster_score_counter += 0.3
                    elif value < 3.4:
                        cluster_score_counter += 0.2
                    elif value >= 3.4:
                        cluster_score_counter += 0.1
                # Multiple cyclic dependent features
                elif value == 10:
                    if value <= 1:
                        cluster_score_counter += 0.3
                    elif value < 4:
                        cluster_score_counter += 0.2
                    elif value >= 4:
                        cluster_score_counter += 0.1
                # Number of features referenced in constraints mean
                elif value == 11:
                    if value <= 0.5:
                        cluster_score_counter += 0.3
                    elif value < 3:
                        cluster_score_counter += 0.2
                    elif value >= 3:
                        cluster_score_counter += 0.1
                # Ratio of variability
                elif value == 12:
                    if value <= 2:
                        cluster_score_counter += 0.3
                    elif value < 4:
                        cluster_score_counter += 0.2
                    elif value >= 4:
                        cluster_score_counter += 0.1
                # Number of valid configurations
                elif value == 13:
                    if value <= 1:
                        cluster_score_counter += 0.3
                    elif value < 3.8:
                        cluster_score_counter += 0.2
                    elif value >= 3.8:
                        cluster_score_counter += 0.1
                # Number of groups or
                elif value == 14:
                    if value <= 1:
                        cluster_score_counter += 0.3
                    elif value < 5:
                        cluster_score_counter += 0.2
                    elif value >= 5:
                        cluster_score_counter += 0.1
                # Number of groups xor
                elif value == 15:
                    if value <= 1:
                        cluster_score_counter += 0.3
                    elif value < 4:
                        cluster_score_counter += 0.2
                    elif value >= 4:
                        cluster_score_counter += 0.1

            number_of_feature_models += 1

    return cluster_score_counter / number_of_feature_models


if __name__ == '__main__':
    base_path = 'k-means/3-clusters/'
    cluster_label_list = ['bad', 'moderate', 'good']
    initial_cluster, final_cluster = 0, 2

    cluster_score_list = []

    for i in range(initial_cluster, final_cluster + 1):
        cluster_score_list.append(
            {'cluster': 'cluster ' + str(i), 'score': get_cluster_score(base_path + 'cluster-' + str(i) + '.csv')})

    cluster_score_list = sorted(cluster_score_list, key=lambda i: i['score'])

    with open(base_path + 'result.txt', 'w') as file:
        for i, cluster_score in enumerate(cluster_score_list):
            file.write(cluster_score['cluster'] +
                       ' : ' + cluster_label_list[i] + ' (' + str(cluster_score['score']) + ')' + '\n')
