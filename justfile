base_dir := env("BUILD_BASE_DIR", justfile_directory())
registry_prefix := "ghcr.io/ultramarine-linux"
tag := "main"
image_suffix := "-shade-bootc"
context := "base"
variant := file_name(context)
image_tag_override := ""
full_tag := ""
image_tag := if image_tag_override != "" {
    image_tag_override
} else {
    registry_prefix + "/" + variant + image_suffix + ":" + tag
}
from := ""
from_arg := if from != "" {
    "--from=" + from
} else {
    ""
}

katsu-live:
    #!/usr/bin/bash -x
    mkdir -p output/
    cp -r scripts/katsu-template/ output/katsu-live/

    IMAGE_NAME="{{ image_tag }}"
    sed -i "s|%BASE_IMAGE%|${IMAGE_NAME}|g" output/katsu-live/bootc-live.yaml

    katsu -o iso output/katsu-live/bootc-live.yaml


pull:
    #!/usr/bin/bash
    podman pull "{{ image_tag }}"
