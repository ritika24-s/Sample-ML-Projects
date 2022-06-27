Task - Your model should learn from the California Housing data and be able to predict the median housing
price in any district, given all the other metrics.

- Frame the problem and look at the big picture -
    - Define the objective in business terms - 
    <!-- model’s output (a prediction of a district’s median housing price) will be fed to another Machine Learning system, along with many other signals. This downstream system will determine whether it is worth investing in a given area or not. Getting this right is critical, as it directly affects revenue. -->
    - How will your solution be used? 
    <!-- answered above -->
    - What are the current solutions/workarounds (if any)?
    <!-- currently estimated manually by experts - costly and time-consuming, and their estimates are not great -->
    - How should you frame this problem (supervised/unsupervised, online/offline, etc.)?
    <!-- supervised  -->
    - How should performance be measured?
    <!-- root mean square error,  -->
    - Is the performance measure aligned with the business objective?
    <!-- Yes, the less the error, the better the predictions and easier to determine if the area is worth investing or not -->
    - What would be the minimum performance needed to reach the business objective?
    - What are comparable problems? Can you reuse experience or tools?
    - Is human expertise available?
    - How would you solve the problem manually?
    - List the assumptions you (or others) have made so far.
    - Verify assumptions if possible.
    <!-- done -->

- Get the data -
    - List the data you need and how much you need.
    <!-- California housing data -->
    - Find and document where you can get that data.
    <!-- from the github repo "https://raw.githubusercontent.com/ageron/handson-ml2/master/" -->
    - Check how much space it will take.
    <!-- 1.3 Mb -->
    - Check legal obligations, and get authorization if necessary.
    <!-- NA -->
    - Get access authorizations.
    <!-- NA -->
    - Create a workspace (with enough storage space).
    <!-- done -->
    - Get the data.
    <!-- created a file download_tgz.py to fetch the data -->
    - Convert the data to a format you can easily manipulate (without changing the data itself).
    <!-- done in function load_housing_data -->
    - Ensure sensitive information is deleted or protected (e.g., anonymized).
    <!-- NA -->
    - Check the size and type of data (time series, sample, geographical, etc.).
    <!-- done in function analyse_data and plot_histogram -->
    - Sample a test set, put it aside, and never look at it (no data snooping!).
    <!-- done in function split_dataset -->

- Explore the data to gain insights
    - Create a copy of the data for exploration (sampling it down to a manageable size if necessary).
    - Create a Jupyter notebook to keep a record of your data exploration.
    - Study each attribute and its characteristics:
        • Name
        • Type (categorical, int/float, bounded/unbounded, text, structured, etc.)
        • % of missing values
        • Noisiness and type of noise (stochastic, outliers, rounding errors, etc.)
        • Possibly useful for the task?
        • Type of distribution (Gaussian, uniform, logarithmic, etc.)
    - For supervised learning tasks, identify the target attribute(s).
    - Visualize the data.
    - Study the correlations between attributes.
    - Study how you would solve the problem manually.
    - Identify the promising transformations you may want to apply.
    - Identify extra data that would be useful (go back to “Get the Data”).
    - Document what you have learned.