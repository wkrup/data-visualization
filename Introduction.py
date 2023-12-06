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

    st.write("## 9조 프로젝트 : 도시-환경 이중 변화 시각화")

    st.sidebar.success("시각화 카테고리를 선택해주세요.")

    st.write(
        """
우리는 땅과 바람, 빛과 자연이 주는 소중함과 가치를 잘 알고 있습니다.  
그와 동시에 기술을 활용하여 누릴 수 있는 편리함도 잘 알고 있습니다.  
그리고 안타깝게도 편리함을 누리면 누릴수록 잃게 되는 많은 것들에 대해,  
디스토피아적인 미래를 예측하는 이들을 외면하면서  
‘아직은 괜찮다’라고 생각하는지도 모릅니다.  
자연이 인간에게 내어준 소중한 가치와 기술이 가능하게 만든 더없이 편리한 미래.  
우리는 지금 어떤 서울에서 살고 있으며 사람들은 어떤 생각을 가지고 있을까요?

    """
    )
    st.image('Image\Intro1.png')

    st.markdown("### 서울에 거주하는 여러가지 이유")
    st.image('Image\Intro2.png')
    st.markdown("### 도시를 구성하는 여러가지 요소")
    st.image('Image\Intro3.png')



if __name__ == "__main__":
    run()
