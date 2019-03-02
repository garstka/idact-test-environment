ARG CONTAINER_CENTOS_VERSION
ARG CONTAINER_SLURM_VERSION

FROM giovtorres/docker-centos${CONTAINER_CENTOS_VERSION}-slurm:${CONTAINER_SLURM_VERSION}

LABEL org.label-schema.name="idact-test-environment"
LABEL org.label-schema.description="Test environment for idact"
LABEL org.label-schema.vcs-url="https://github.com/garstka/idact-test-environment"
LABEL maintainer="Matt Garstka"

ARG CONTAINER_CENTOS_VERSION
ARG CONTAINER_PYTHON_VERSION
ARG CONTAINER_USERS

ENV CONTAINER_CENTOS_VERSION=$CONTAINER_CENTOS_VERSION
ENV CONTAINER_PYTHON_VERSION=$CONTAINER_PYTHON_VERSION
ENV CONTAINER_USERS=$CONTAINER_USERS
COPY setup/install_python.py /root/
COPY setup/adjust_configs.py /root/
COPY setup/ssh_install.py /root/
COPY setup/ssh_generate_host_keys.py /root/
COPY setup/add_users.py /root/
COPY setup/install_jupyter.py /root/
COPY setup/install_dask.py /root/
COPY setup/srun_mock.py /usr/local/bin/srun
COPY setup/install_srun_mock.py /root/
COPY setup/install_stress.py /root/
COPY setup/adjust_entrypoint.py /root/
RUN python /root/install_python.py && \
	python$CONTAINER_PYTHON_VERSION /root/adjust_configs.py && \
	python$CONTAINER_PYTHON_VERSION /root/ssh_install.py && \
	python$CONTAINER_PYTHON_VERSION /root/ssh_generate_host_keys.py && \
	python$CONTAINER_PYTHON_VERSION /root/add_users.py  && \
	python$CONTAINER_PYTHON_VERSION /root/install_jupyter.py && \
	python$CONTAINER_PYTHON_VERSION /root/install_dask.py  && \
	python$CONTAINER_PYTHON_VERSION /root/install_srun_mock.py  && \
	python$CONTAINER_PYTHON_VERSION /root/install_stress.py && \
	python$CONTAINER_PYTHON_VERSION /root/adjust_entrypoint.py && \
	rm \
	/root/install_python.py \
	/root/adjust_configs.py \
	/root/ssh_install.py \
	/root/ssh_generate_host_keys.py \
	/root/add_users.py \
	/root/install_jupyter.py \
	/root/install_dask.py \
	/root/install_srun_mock.py \
	/root/install_stress.py \
	/root/adjust_entrypoint.py
