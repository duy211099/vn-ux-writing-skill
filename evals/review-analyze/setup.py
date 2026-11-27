"""Set up a temp repo for one review/analyze eval case.

Usage: python3 setup.py <case> <dest>
  R-01, R-02, R-05  fixture-mixed, git init + commit (R-01/R-05 then apply the change)
  R-03a             fixture-mixed copied with no git at all
  R-03b             fixture-mixed in a fresh `git init` with no commits
  R-04              fixture-big, git init + commit
  R-06              fixture-mixed; branch `feature` commits the R-01 `cart.empty`
                    change and the opening paragraph; then `main` moves on
                    (a `profile.saved` change in src/account/locales/vi.json and
                    the `## Lời kết` paragraph); `feature` is checked out, clean

R-01 change: `cart.empty` in src/locales/vi.json (staged) and two
paragraphs of docs/blog/ra-mat.md (left unstaged).
"""

import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent

CART_OLD = '"empty": "Giỏ hàng của bạn trống"'
CART_NEW = '"empty": "Giỏ hàng của bạn hiện đang trống. Vui lòng thêm sản phẩm vào giỏ hàng."'

P1_OLD = (
    "Có những món ăn không chỉ để no bụng, mà còn kể một câu chuyện về cả một vùng đất. "
    "Phở Hà Nội là một món như thế: một bát nước trong, vài lát thịt bò, sợi bánh mềm mượt, "
    "và cả một thế kỷ ký ức của người Hà Nội."
)
P1_NEW = (
    "Trong thời đại công nghệ 4.0, việc thưởng thức một bát phở chuẩn vị chưa bao giờ dễ dàng đến thế. "
    "Từ ngày 1/12/2026, Bếp Nhà không chỉ giao phở tận nơi từ 6:30 sáng ở quận Hoàn Kiếm và Ba Đình, "
    "mà còn mang đến trải nghiệm ẩm thực tuyệt vời ngay tại ngôi nhà của bạn."
)
P2_OLD_START = "Phở Hà Nội không cầu kỳ, không phô trương"
P2_NEW = (
    "Tóm lại, Bếp Nhà là giải pháp hoàn hảo cho những ai yêu phở nhưng không có thời gian ra quán. "
    "Đơn đầu tiên được giảm 30.000đ khi nhập mã PHOSANG. "
    "Hãy tải ứng dụng và trải nghiệm ngay hôm nay!"
)


def git(dest: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(dest), *args], check=True, capture_output=True)


def init_commit(dest: Path) -> None:
    git(dest, "init", "-q", "-b", "main")
    git(dest, "-c", "user.name=Eval", "-c", "user.email=eval@example.com", "add", "-A")
    git(dest, "-c", "user.name=Eval", "-c", "user.email=eval@example.com",
        "commit", "-q", "-m", "Initial")


def apply_r01(dest: Path) -> None:
    vi = dest / "src/locales/vi.json"
    text = vi.read_text(encoding="utf-8")
    assert CART_OLD in text
    vi.write_text(text.replace(CART_OLD, CART_NEW), encoding="utf-8")
    git(dest, "add", "src/locales/vi.json")

    post = dest / "docs/blog/ra-mat.md"
    lines = post.read_text(encoding="utf-8").split("\n")
    assert P1_OLD in lines
    lines[lines.index(P1_OLD)] = P1_NEW
    i = next(k for k, line in enumerate(lines) if line.startswith(P2_OLD_START))
    lines[i] = P2_NEW
    post.write_text("\n".join(lines), encoding="utf-8")


ACCOUNT_OLD = '"saved": "Thông tin của quý khách đã được cập nhật thành công"'
ACCOUNT_NEW = '"saved": "Đã cập nhật thông tin tài khoản"'
GIT_ID = ["-c", "user.name=Eval", "-c", "user.email=eval@example.com"]


def commit_all(dest: Path, msg: str) -> None:
    git(dest, "add", "-A")
    git(dest, *GIT_ID, "commit", "-q", "-m", msg)


def setup_r06(dest: Path) -> None:
    init_commit(dest)
    git(dest, "checkout", "-q", "-b", "feature")
    vi = dest / "src/locales/vi.json"
    vi.write_text(vi.read_text(encoding="utf-8").replace(CART_OLD, CART_NEW), encoding="utf-8")
    post = dest / "docs/blog/ra-mat.md"
    text = post.read_text(encoding="utf-8")
    assert P1_OLD in text
    post.write_text(text.replace(P1_OLD, P1_NEW), encoding="utf-8")
    commit_all(dest, "Feature: launch copy")

    git(dest, "checkout", "-q", "main")
    acc = dest / "src/account/locales/vi.json"
    text = acc.read_text(encoding="utf-8")
    assert ACCOUNT_OLD in text
    acc.write_text(text.replace(ACCOUNT_OLD, ACCOUNT_NEW), encoding="utf-8")
    lines = post.read_text(encoding="utf-8").split("\n")
    i = next(k for k, line in enumerate(lines) if line.startswith(P2_OLD_START))
    lines[i] = "Phở Hà Nội ngon nhất vào buổi sáng, khi nồi nước dùng vừa mở."
    post.write_text("\n".join(lines), encoding="utf-8")
    commit_all(dest, "Main: account copy and closing")
    git(dest, "checkout", "-q", "feature")


def main(case: str, dest: str) -> None:
    out = Path(dest)
    if out.exists():
        sys.exit(f"{out} exists")
    src = HERE / ("fixture-big" if case == "R-04" else "fixture-mixed")
    shutil.copytree(src, out)
    if case == "R-03a":
        return
    if case == "R-06":
        setup_r06(out)
        return
    if case == "R-03b":
        git(out, "init", "-q", "-b", "main")
        return
    init_commit(out)
    if case in ("R-01", "R-05"):
        apply_r01(out)


if __name__ == "__main__":
    main(*sys.argv[1:])
