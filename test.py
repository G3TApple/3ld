def nelder_mead(f, starting_point, tolerance=0.001):
    # Stat tracing
    triangles = []
    function_calls = 0

    # Generate Simplex Points
    simplex = generate_points(f, starting_point)
    function_calls += len(simplex)

    n = len(simplex) - 1  # Number of variables

    for i in range(1, 50):
        # Select Worst Point
        worst_points_index = find_worst_points_index(simplex)

        # Find Centroid
        centroid = find_centroid(f, simplex, n, worst_points_index)
        function_calls += 1

        # Reflection
        xr = step(f, simplex, centroid, worst_points_index, 1)
        function_calls += 1

        triangles.append(copy.deepcopy(simplex))  # Stats

        # Try Expansion
        if (
                xr["value"] <= simplex[find_best_points_index(simplex)]["value"]
        ):  # F(x_r) <= F(x^(0))
            xe = step(f, simplex, centroid, worst_points_index, 2)
            function_calls += 1

            if (
                    xe["value"] <= simplex[find_best_points_index(simplex)]["value"]
            ):  # F(x_e) <= F(x^(0))
                simplex[worst_points_index] = xe
            else:
                simplex[worst_points_index] = xr
        # Reflected is fine
        elif xr["value"] <= simplex[find_second_worst_points_index(simplex)]["value"]:
            simplex[worst_points_index] = xr
        # Inside contraction
        elif xr["value"] >= simplex[worst_points_index]["value"]:
            xic = step(f, simplex, centroid, worst_points_index, -0.5)
            function_calls += 1

            if xic["value"] <= simplex[worst_points_index]["value"]:
                simplex[worst_points_index] = xic
            # Shrink
            else:
                simplex = shrink(f, simplex)
                function_calls += n
        # Outside contraction
        else:
            xoc = step(f, simplex, centroid, worst_points_index, 0.5)
            function_calls += 1

            if xoc["value"] <= simplex[worst_points_index]["value"]:
                simplex[worst_points_index] = xoc
            # Shrink
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