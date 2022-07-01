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
    jobs_list = []

    for job in jobs:
        try:
            compatible_job = matches_salary_range(job, salary)
        except Exception:
            next
        else:
            if compatible_job:
                jobs_list.append(job)

    return jobs_list
