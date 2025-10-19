def nelder_mead(f, starting_point, tolerance=0.001):
    triangles = []
    function_calls = 0

    simplex = generate_points(f, starting_point)
    function_calls += len(simplex)

    n = len(simplex) - 1

    for i in range(1, 50):
        worst_points_index = find_worst_points_index(simplex)

        centroid = find_centroid(f, simplex, n, worst_points_index)
        function_calls += 1

        xr = step(f, simplex, centroid, worst_points_index, 1)
        function_calls += 1

        triangles.append(copy.deepcopy(simplex))

        if (
                xr["value"] <= simplex[find_best_points_index(simplex)]["value"]
        ):
            xe = step(f, simplex, centroid, worst_points_index, 2)
            function_calls += 1

            if (
                    xe["value"] <= simplex[find_best_points_index(simplex)]["value"]
            ):
                simplex[worst_points_index] = xe
            else:
                simplex[worst_points_index] = xr
        elif xr["value"] <= simplex[find_second_worst_points_index(simplex)]["value"]:
            simplex[worst_points_index] = xr
        elif xr["value"] >= simplex[worst_points_index]["value"]:
            xic = step(f, simplex, centroid, worst_points_index, -0.5)
            function_calls += 1

            if xic["value"] <= simplex[worst_points_index]["value"]:
                simplex[worst_points_index] = xic
            else:
                simplex = shrink(f, simplex)
                function_calls += n
        else:
            xoc = step(f, simplex, centroid, worst_points_index, 0.5)
            function_calls += 1

            if xoc["value"] <= simplex[worst_points_index]["value"]:
                simplex[worst_points_index] = xoc
            else:
                simplex = shrink(f, simplex)
                function_calls += n

        if (
                np.linalg.norm(
                    simplex[find_worst_points_index(simplex)]["coords"]
                    - simplex[find_best_points_index(simplex)]["coords"]
                )
                <= tolerance
        ):
            break

    return simplex, triangles, function_calls