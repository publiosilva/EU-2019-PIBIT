def get_cluster_score(cluster_path):
    number_of_feature_models = 0
    cluster_score_counter = 0

    with open(cluster_path) as file:
        for line in file:
            columns = line.split(',')

            # Feature EXtendibility (FEX) and Flexibility of configuration (FoC)
            directly_proportional_values_columns = [7, 8]

            for i, column in enumerate(columns):
                if i > 0:
                    if i in directly_proportional_values_columns:
                        if column == 'veryLow':
                            cluster_score_counter += 1
                        elif column == 'low':
                            cluster_score_counter += 2
                        elif column == 'moderate':
                            cluster_score_counter += 3
                        elif column == 'high':
                            cluster_score_counter += 4
                        elif column == 'veryHigh':
                            cluster_score_counter += 5
                    else:
                        if column == 'veryLow':
                            cluster_score_counter += 5
                        elif column == 'low':
                            cluster_score_counter += 4
                        elif column == 'moderate':
                            cluster_score_counter += 3
                        elif column == 'high':
                            cluster_score_counter += 2
                        elif column == 'veryHigh':
                            cluster_score_counter += 1

            number_of_feature_models += 1

    return cluster_score_counter / number_of_feature_models


if __name__ == '__main__':
    cluster_score_list = []
    cluster_label_list = ['very bad', 'bad', 'moderate', 'good', 'very good']

    for i in range(0, 5):
        cluster_score_list.append(
            {'cluster': 'cluster ' + str(i), 'score': get_cluster_score('cluster-' + str(i) + '.csv')})

    cluster_score_list = sorted(cluster_score_list, key=lambda i: i['score'])

    with open('result.txt', 'w') as file:
        for i, cluster_score in enumerate(cluster_score_list):
            file.write(cluster_score['cluster'] +
                       ' : ' + cluster_label_list[i] + '\n')
