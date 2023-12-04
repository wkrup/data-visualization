# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Data Visualization Project: Team 9",
    )

    st.write("# 9조 프로젝트: 도시-환경 이중 변화 시각화")

    st.sidebar.success("시각화 카테고리를 선택해주세요.")

    st.markdown(
        """
        인트로 내용
        ### 인트로 1.1
        - 1.1.1
        - 1.1.2
        ### 인트로 내용 1.2
        - 1.2.1
        - 1.2.2
    """
    )


if __name__ == "__main__":
    run()
