from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    types = [job["job_type"] for job in jobs]

    return set(types)


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    industries = read(path)
    industry = [i["industry"] for i in industries if i["industry"] != ""]

    return set(industry)


print(get_unique_industries("src/jobs.csv"))


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    data = read(path)
    salaries = [
        int(salary["max_salary"])
        for salary in data
        if salary["max_salary"].isnumeric()
    ]

    return max(salaries)


def get_min_salary(path):
    data = read(path)
    salaries = [
        int(salary["min_salary"])
        for salary in data
        if salary["min_salary"].isnumeric()
    ]

    return min(salaries)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if not ("max_salary" in job) or not ("min_salary" in job):
        raise ValueError()

    if (
        type(job["min_salary"])
        or type(job["max_salary"])
        or type(salary)
    ) != int:
        raise ValueError()

    if job["min_salary"] > job["max_salary"]:
        raise ValueError()

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
